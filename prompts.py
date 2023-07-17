

# initial prompt
initial_question_prompt = """
Your task is to develop questions that can be used in a podcast.
Create questions for company {company_name}

Your task is to develop questions to be asked in this podcast about the digital transformation of {company_name}
This is the part of the podcast, where initial questions are asked, that aim to kickstart the discussion.
Make the questions funny and interesting.
List the questions while numbering them.

"""

dt_find_unmentioned_segments = """
You are interviewing a guest about the business model transformation of his company, that happened during the digital transformation of his company. 
The Digital transformation influences many parts of the business model.
A business model consists of the following components: Client segments, client relationships, value proposition, resources, channels, activities, partnerships, financials

Given an answer about the digital transformation your task is to find the components of the business model that were not talked on in the guest's answer.
List the components one by one each in a new text line, if they were not mentioned or similar things were not mentioned.
After that for each identified component, generate a question about it, so that the guest tells about the aspect of that component in the digital transformation of his company.
Write each identified component and the question right after it in a new line. Each should be written in a new line.
Example:

Client segments: What did change in the client segments?

Value proposition: Did you find new ways to provide value to your customers using the same product?

Guest's answer:
{answer}
"""

dt_find_contents = """
You are given components of the business model. For each of these components find the contents and list the elements contained by their waves, aswell as the subelements of each wave if they existe.g.:
Classical:
 - element 1
 - element 2
   - subelement 1

Wave 1:
 - element 1
   - subelement 1
   - subelement 2

And so on

{components}

"""

#
podcast_structure_planning_template_eng = """
You are a professional host
Your task is to plan a podcast structure according to the requirements specified further below.
The structure has to be written as a list of sections that the podcast will cover.
For example if the podcast has three sections, e.g. introduction, middle and end, the structure has to be written with each section in a new line and numbered as following:
1. introduction
2. middle
3. end

This is the requirements for the podcast:
{requirements}
"""

podcast_structure_planning_template = """
Du bist ein professioneller Podcast-Gastgeber
Weiter unten sind Informationen zu Deinem heutigen Gast und seinem Hintergrund spezifiziert.
Du hast eine intensive Recherche durchgeführt, um möglichst viele Informationen einzuholen, die dir beim heutigen Thema behilflich sein können. Diese findest du weiter unten unter Recherche.
Genaue Anforderungen sind ebenso weiter unten spezifiziert.
Deine Aufgabe besteht darin, einen Podcast maßgeschneidert an deinen Gast, basierend auf der Recherche und gemäß den weiter unten aufgeführten Anforderungen zu planen.

Informationen zum Gast und seinem Hintergrund:
{background_information}

Das sind die Voraussetzungen für den Podcast:
{requirements}

Recherche:
{research}

Folgend ist ein Beispiel mit Abschnitten, welche Themen ein Podcast abdecken kann, auf die er sich aber nicht beschränken muss:
Strategien: Welche unterschiedlichen Strategien nutzen Unternehmen bei der digitalen Transformation?
Herausforderungen: Was sind die typischen Herausforderungen, mit denen ein Unternehmen während der digitalen Transformation konfrontiert sein könnte, und wie können diese gemildert werden?
Best Practices: Was sind die Best Practices für die digitale Transformation? Was hat bei einigen Unternehmen gut funktioniert, wovon andere lernen können?
Rolle der Mitarbeiter: Wie wirkt sich die digitale Transformation auf die Mitarbeiter aus? Welche Rolle spielen sie im Transformationsprozess und wie können sie am besten unterstützt werden?
Technologien: Welche neuesten Technologien helfen bei der digitalen Transformation? Wie werden KI, maschinelles Lernen, Blockchain und andere Technologien genutzt?
Zukünftige Trends: Was sind die zukünftigen Trends in der digitalen Transformation? Wie wird es sich weiterentwickeln?
Branchenspezifische Besonderheiten: Wie unterscheidet sich die digitale Transformation in den verschiedenen Branchen? Welche branchenspezifischen Überlegungen oder Herausforderungen gibt es?
Lessons Learned: Was sind die wichtigsten Lehren aus gescheiterten Initiativen zur digitalen Transformation?


Dabei soll der Podcast-Plan im JSON-Format als hierarchische Struktur mit Abschnitten als Schlüssel und dazugehörigen Fragen oder Themen als Liste definiert werden.
Dabei soll immer eine Einführung enthalten sein und ein Schlussteil. Diese sollen immer als "Einführung" und "Schlussteil" bezeichnet werden.
Beispiel:
{json_example}

Deine Antwort:
"""

podcast_structure_json_example = """{
  "Einleitung": ["wer ist unser Gast heute", "Was hat er Tolles gemacht"],
  "Thema1": ["Interessantes zum Thema 1", "Was kann man lernen"],
  "Thema2": ["Interessantes zum Thema 2", "Frage 1", "Frage2"],
  "Schlussteil": ["Recap", "Mögliche Themen zum nächsten Podcast"]
}"""

podcast_structure_context_queries = """
Du sind ein professioneller Podcast-Gastgeber
Weiter unten sind Informationen zu Deinem heutigen Gast und seinem Hintergrund spezifiziert.
Genaue Anforderungen sind ebenso weiter unten spezifiziert.
Deine Aufgabe besteht darin, einen Podcast maßgeschneidert an deinen Gast, basierend auf der Recherche und gemäß den weiter unten aufgeführten Anforderungen zu planen.

Du bist zu einer Vector Database verbunden, die theoretische Informationen zu dem Thema enthält wie zum Beispiel Definitionen, Modelle und so weiter, die dir helfen sollen, die Anforderung zu verstehen und umzusetzen.
Folgende Dokumente hast du erhalten: {document_name_list}. Deren Namen sollen dir einen Hinweis darüber geben, welche Informationen diese enthalten können.
Die folgende Anforderung hast du erhalten: {requirements}
Folgende Informationen zum Gast und seinem Hintergrund hast du erhalten: {background_information}
Generiere genau 10 Anfragen, auf deren Basis die Vector-Datenbank durchgesucht werden kann, um mehr Informationen zum Kontext im Rahmen der Anforderungen und Hintergrund des Gastes einzuholen.
Schreibe jede Anfrage hintereinande ohne Nummerierung und trenne sie dabei untereinander durch folgendes Symbol: *
Beispiel:
Was ist A*Was ist B
"""