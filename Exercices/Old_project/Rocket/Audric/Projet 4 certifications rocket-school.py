# Projet 4 certifications rocket-school

print("renseigne ton score")
score_certif = input()


if int(score_certif) > 90:
    print("Certification obtenue, niveau expert")
elif int(score_certif) > 80:
    print("Certification obtenue, niveau confirmé")
elif int(score_certif) > 70:
    print("Certification obtenue, niveau intermédiaire")
elif int(score_certif) > 65:
    print("Certification obtenue")
else:
    int(score_certif) < 65
    print("Repassez votre certification")



