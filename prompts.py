

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


Dabei soll der Podcast-Plan im JSON-Format als hierarchische Struktur mit Abschnitten als Schlüssel und dazugehörigen Fragen oder Inhalt als Liste definiert werden.
Dabei soll immer eine Einführung enthalten sein und ein Schlussteil. Diese sollen immer als "Einführung" und "Schlussteil" bezeichnet werden.
Bei Einleitung und Schlussteil sollten keine Fragen vorkommen, sondern Inhalt wie z.B. Begrüßung des Gastes und so weiter. Im Schlussteil sollten neben einem Recap ggf. weitere Themen vorkommen.
Die Schlüssel anderer Abschnitte als Einleitung und Schlussteil sollen einen passenden Namen tragen, der das Wesen des Abschnitts umreißt, z.B. Automatisierung.
Anders als bei Einleitung und Schlussteil können die anderen Abschnitte Fragen und Inhalte beinhalten, sie müssen mindestens 5 Fragen oder Fragen mit Inhalten beinhalten.
Wenn zum Beispiel der Abschnitt über Automatisierung ist und in der Recherche ein interessanter Fakt vorkommt, der zum Abschnitt passt und der helfen könnte die Diskussion anzustoßen, schreibe diesen Fakt hin und generiere eine passende Frage.
Die Fragen sollten immer an den Gast und seine Erfahrungen gerichtet sein und somit oft mit seinem Namen beginnen, wie: Herr Mustermann, hatten Sie die gleiche Erfahrung gemacht?
Nachfolgend ein Beispiel eines kurzen Podcast-Plans im JSON-Format
Beispiel:
{json_example}

Deine Antwort:
"""

podcast_structure_json_example = """{
  "Einleitung": ["Begrüßung und Vorstellung des Gastes", "Besprechung des heutigen Themas"],
  "Prozessautomatisierung": ["Firma X hat einen Prozess automatisiert und dabei im gleichen Jahr einen 20% höheren Gewinn gemacht. Haben Sie die gleiche Erfahrung gemacht?", "Was kann man daraus lernen?"],
  "Anderes Thema": ["Interessantes zum anderen Thema", "Frage 1", "Frage2"],
  "Schlussteil": ["Recap", "Mögliche Themen zum nächsten Podcast"]
}"""

podcast_structure_context_queries = """
Du bist ein professioneller Podcast-Gastgeber mit jahrelanger Erfahrung in Podcast-Planung und -Durchführung.
Für einen Podcast, der maßgeschneidert an deinen fiktiven Gast mit seinem Hintergrund, speziellen Anforderungen an den Podcast und verfügbaren Dokumenten führst du eine Recherche durch.
Bei dieser Recherche hast du Zugang zu einer Vektordatenbank, die du nach Informationen aus Dokumenten abfragen kannst.
Weiter unten sind Hintergrundinformationen zum Gast, Anforderungen an den Podcast, sowie Zusammenfassungen der in der Datenbank enthaltenen Dokumente spezifiziert.

Hintergrundinformationen zum fiktiven Gast:
{background_information}

Anforderungen an den Podcast:
{requirements}

Zusammenfassungen der in der Datenbank enthaltenen Dokumente:
{summaries}

Deine Aufgabe ist nun Anfragen zu schreiben, auf Basis derer die Datenbank abgefragt wird, um eine hochqualitative Recherche zu garantieren.

Generiere genau 10 Anfragen, auf deren Basis die Vector-Datenbank durchgesucht werden kann, um mehr Informationen zum Kontext im Rahmen der Anforderungen und Hintergrund des Gastes einzuholen.
Jede Anfrage soll genau eine Frage beinhalten.
Schreibe jede Anfrage hintereinande ohne Nummerierung und trenne sie dabei untereinander durch folgendes Symbol: *
Beispiel:
Was ist A*Was ist B

Deine Antwort:
"""

podcastxxx = """
Du bist ein professioneller Podcast-Gastgeber mit jahrelanger Erfahrung in Podcast-Planung und -Durchführung.
Für einen Podcast, der maßgeschneidert an deinen fiktiven Gast mit seinem Hintergrund, speziellen Anforderungen an den Podcast und verfügbaren Dokumenten führst du eine Recherche durch.
Bei dieser Recherche hast du Zugang zu einer Vektordatenbank, die du nach Informationen aus Dokumenten abfragen kannst.
Weiter unten sind Hintergrundinformationen zum Gast, Anforderungen an den Podcast, sowie Zusammenfassungen der in der Datenbank enthaltenen Dokumente spezifiziert.

Hintergrundinformationen zum fiktiven Gast:
{background_information}

Anforderungen an den Podcast:
{requirements}

Zusammenfassungen der in der Datenbank enthaltenen Dokumente:
{summaries}

Deine Aufgabe ist nun Anfragen zu schreiben, auf Basis derer die Datenbank abgefragt wird, um eine hochqualitative Recherche zu garantieren.

Beispielhafte Informationen:

Hintergrundinformationen zum fiktiven Gast:
Max Mustermann ist der CEO eines Unternehmens das selbstfahrende Autos produziert.
Nach einer Digitalen Transformation wurde die Produktion vollständig automatisiert, was sowohl die Warenhausverwaltung, als auch die Montage beinhaltet.


Anforderungen an den Podcast:
Zielgruppe: Akademiker
Dauer des Podcast: 1 Stunde
Minimale Anzahl von Fragen: 15
SEO-Keywords: Industrie 4.0, KI in der Fertigung, Nachhaltige Produktion, Autonome Produktionssysteme, Soziale Auswirkungen der Produktion Automatisierung
Kernbotschaft: Automatisierung in der Produktion steigert Effizienz und Qualität, erfordert jedoch einen sorgfältigen Umgang mit sozialen und arbeitsrechtlichen Fragen. Ein verantwortungsvoller Ansatz kann zu einer nachhaltigen, technologieorientierten Produktionszukunft führen, die für alle von Vorteil ist.

Zusammenfassungen der in der Datenbank enthaltenen Dokumente:
In dieser Fallstudie wurde eine Produktionsstätte erfolgreich und vollständig automatisiert, um Effizienz und Produktivität zu steigern. Durch den Einsatz von KI und Roboter-Technologie wurde der Produktionsprozess optimiert und Fehler reduziert. Dies führte zu einer signifikanten Kosteneinsparung und erhöhte gleichzeitig die Produktqualität. Allerdings führte die Automatisierung auch zu sozialen und arbeitsrechtlichen Herausforderungen, die sorgfältig angegangen werden mussten.
Dieser Artikel untersucht das Konzept der digitalen Transformation (DT) von Geschäftsmodellen und untersucht die für die DT notwendigen Ressourcen wie Finanzkapital, digitale Ressourcen, das WWW, Suchmaschinen, Internetinhalte und Apps. Es werden der Wertversprechen-/Vorteilsbereich, die Kanäle und der Kundenerlebnisbereich, der Finanz- und Wirtschaftsbereich sowie der Aktivitäten- und Energieverbrauchsbereich von DT besprochen. Es bietet Einblicke und fördert den Einsatz eines „Business Model Canvas“ als Rahmen für die konzeptionelle Umstrukturierung von Organisationen. Es ermutigt die Leser, sich darum zu bemühen, die rasanten Veränderungen zu verstehen, die sich in der Welt durch die digitale Transformation ergeben.

Beispielhafter Gedankengang:
Da das Unternehmen selbst
"""

podcast_document_summarize_prompt = """
Schreibe eine Zusammenfassung 
"""