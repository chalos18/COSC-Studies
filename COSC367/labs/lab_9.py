def posterior(prior, likelihood, observation):
    """
    Compute the posterior probability using Bayes' theorem.

    Parameters:
    prior (float): a real number representing p(Class-true). The probability p(Class-false) can be obtained as 1 - prior.
    likelihood (float): tuple of length n where each element is a pair of real numbers such that likelihood[i][false] is p(X[i]=true|C=false) and likelihood[i][True] is p(X[i]=true|C=true ).
      That is, likelihood contains the 2*n CPTs that are required at leaf nodes.
    observation (float): tuple of n Booleans such that observation[i] is the observed value T or F for the input feature X[i].

    Returns:
    float: returns p(Class=true|observation).
    """
    lik_true = 1
    lik_false = 1
    n = len(observation)

    for i in range(n):
        obs = observation[i]
        prob_false, prob_true = likelihood[i]

        if obs:
            # X[i] is True
            lik_true *= prob_true
            lik_false *= prob_false
        else:
            # X[i] is False
            lik_true *= 1 - prob_true
            lik_false *= 1 - prob_false

    numerator = prior * lik_true
    evidence = prior * lik_true + (1 - prior) * lik_false

    return numerator / evidence


prior = 0.05
likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

observation = (True, True, True)

# class_posterior_true = posterior(prior, likelihood, observation)
# print("P(C=False|observation) is approximately {:.5f}".format(1 - class_posterior_true))
# print("P(C=True |observation) is approximately {:.5f}".format(class_posterior_true))

import csv


def learn_prior(file_name, pseudo_count=0):
    """
    Returns a real number that is the prior probability of spam being true
    Prior probability is the probability that an email is spam before considering any specific feature of the email
    """
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]

    spam_count = 0
    for x in training_examples:
        # The last column of a tuple is the class (spam or not)
        # features = len(x) - 1
        spam = x[-1]
        if spam == "1":
            spam_count += 1

    total_count = len(training_examples) - 1
    prior = (spam_count + pseudo_count) / (total_count + 2 * pseudo_count)

    return prior


# prior = learn_prior("/home/anaoliveira/workspace/study-prep/COSC367/spam-labelled.csv")
# print("Prior probability of spam is {:.5f}.".format(prior))

# prior = learn_prior("/home/anaoliveira/workspace/study-prep/COSC367/spam-labelled.csv")
# print("Prior probability of not spam is {:.5f}.".format(1 - prior))


def learn_likelihood(file_name, pseudo_count=0):
    """
    Returns a seequence of pairs of likelihood probabilities.
    Each element in the sequence is a pair (tuple) of real numbers such that likelihood[i][False] is P(X[i]=true|Spam=false) and likelihood[i][True] is P(X[i]=true|Spam=true ).
    """
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]

    spam_T = 0
    spam_F = 0
    likelihood = []
    occurences = {column: (0, 0) for column in range(len(training_examples[0]) - 1)}
    for email in training_examples:
        # The last column of a tuple is the class (spam or not)
        # features = len(x) - 1
        spam = email[-1]
        if spam == "1":
            spam_T += 1
        if spam == "0":
            spam_F += 1

        for column, i in enumerate(email):
            if column != len(email) - 1:
                # true given false
                if i == "1" and email[-1] == "0":
                    true, false = occurences[column]
                    false += 1
                    occurences[column] = (true, false)
                # true given true
                if i == "1" and email[-1] == "1":
                    true, false = occurences[column]
                    true += 1
                    occurences[column] = (true, false)

    # total_count = len(training_examples) - 1
    for count in occurences:
        true, false = occurences[count]
        likelihood.append(
            (
                (false + pseudo_count) / (spam_F + pseudo_count * 2),
                (true + pseudo_count) / (spam_T + pseudo_count * 2),
            )
        )

    # print(likelihood)
    # likelihood["P(Spam)"] = (spam_T / total_count, spam_F / total_count)

    return likelihood


# likelihood = learn_likelihood(
#     "/home/anaoliveira/workspace/study-prep/COSC367/spam-labelled.csv"
# )
# print(len(likelihood))
# print([len(item) for item in likelihood])

# print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
# print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
# print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
# print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))


# likelihood = learn_likelihood(
#     "/home/anaoliveira/workspace/study-prep/COSC367/spam-labelled.csv", pseudo_count=1
# )

# print("With Laplacian smoothing:")
# print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
# print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
# print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
# print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

def nb_classify(prior, likelihood, input_vector):
    """
    classifies an unseen input vector that is a tuple of 12 integers, 0 or 1 corresponding to attributes.
    returns a tuple pair where the first element is either spam or not spam, and the second element is the certainty
    the certainty is the probability of spam when the instance is classified as spam, or the prob of not spam otherwise.
    if qual likely then choose not spam
    """
    classification = posterior(prior, likelihood, input_vector)

    if classification > 0.5:
        spam = ("Spam", classification)
        return spam
    else:
        not_spam = ("Not Spam", 1-classification)
        return not_spam


prior = learn_prior("/home/anaoliveira/workspace/study-prep/COSC367/spam-labelled.csv")
likelihood = learn_likelihood("/home/anaoliveira/workspace/study-prep/COSC367/spam-labelled.csv")

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))
