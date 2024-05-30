# StudyBot Evaluation

In diesem Projekt wird das Ergebnis meiner Studienarbeit an der DHBW Mosbach evaluiert. Für die Arbeit sollte ein Chatbot erstellt werden, der Fragen zu den Leitlinien beantworten kann.

## Aufbau

Das Django Projekt dient als Schicht zwischen dem User und dem Chatbot Framework PrivateGPT (https://github.com/zylon-ai/private-gpt).

Die Kommunikation mit dem Projekt ist über den API-Client Bruno (https://www.usebruno.com/) gedacht, für welchen hier auch ein Profil im Ordner "/bruno" vorhanden ist.

In der Evaluierung_StudyBot.xlsx sind die Ergebnisse der Untersuchung zusammengefasst.

## Setup

Für die Verwendung ist eine lokale PrivateGPT-Instanz notwendig. Das verwendete Sprachmodell für die Evaluierung ist Mistral 7B.