
podcast_topics_generation_template = """
Du bist ein professioneller Podcast-Gastgeber mit jahrelanger Erfahrung in Podcast-Planung und -Durchführung.
Für einen Podcast, der maßgeschneidert an deinen fiktiven Gast und seinen Hintergrund, sowie weiteren Anforderungen angepasst sein soll, sollst du mögliche Themen vorschlagen.
In den Anforderungen können, müssen aber nicht folgende Informationen enthalten sein. Falls sie enthalten sind berücksichtige diese bitte. Wenn eine Anforderung nicht weiter spezifiziert ist, steht bei ihr als Inhalt "UNDEFINED".

Die Themen sollen zum Hintergrund des Gastes und seinen Erfahrungen passen. Zum Beispiel Falls der Gast ein Profi in der Digitalen Transformation ist, sollen Themen vorgeschlagen werden, über die er sprechen könnte.
Hintergrundinformationen zum Gast:
{bg_info}

Die Themen sollen zur Zielgruppe passen und dabei die Eigenschaften der Zielgruppe berücksichtigen. Akademiker würden zum Beispiel komplexere Themen bevorzugen.
Zielgruppe:
{target_audience}

Das ist die Botschaft, die die Hörer am Ende des Podcasts verstanden haben sollen
Kernbotschaft:
{message} 

Diese Wörter sollen so oft es geht in der Wortwahl verwendet werden, ohne den Sinn des Inhalts maßgeblich zu beeinflussen.
SEO-Keywords:
{keywords}

Falls hier enthalten, können diese Hinweise auf mögliche Themen geben.
Fragen: 
{questions}

Schreib genau 10 Themenvorschläge, die zu den oben genannten Anforderungen passen hintereinande ohne Nummerierung und trenne sie dabei untereinander durch folgendes Symbol: *
Sie sollen UNBEDINGT durch folgendes Symbol getrennt werden: *
Sie dürfen KEINESWEGS nummeriert sein.
Beispiel:
Was ist A*Was ist B*Was ist C

Deine Antwort:
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

Die Inhalte des Podcast sollen zum Thema genau passen
Thema des Podcast:
{topic}

Die Themen sollen zum Hintergrund des Gastes und seinen Erfahrungen passen. Zum Beispiel Falls der Gast ein Profi in der Digitalen Transformation ist, sollen Themen vorgeschlagen werden, über die er sprechen könnte.
Hintergrundinformationen zum Gast:
{bg_info}

Die Themen sollen zur Zielgruppe passen und dabei die Eigenschaften der Zielgruppe berücksichtigen. Akademiker würden zum Beispiel komplexere Themen bevorzugen.
Zielgruppe:
{target_audience}

Das ist die Botschaft, die die Hörer am Ende des Podcasts verstanden haben sollen
Kernbotschaft:
{message} 

Diese Wörter sollen so oft es geht in der Wortwahl verwendet werden, ohne den Sinn des Inhalts maßgeblich zu beeinflussen.
SEO-Keywords:
{keywords}

Falls hier enthalten, können diese Hinweise auf mögliche Themen geben.
Fragen: 
{questions}

Zusammenfassungen der in der Datenbank enthaltenen Dokumente:
{summaries}

Deine Aufgabe ist nun Anfragen zu schreiben, auf Basis derer die Datenbank abgefragt wird, um eine hochqualitative Recherche zu garantieren.

Generiere genau 10 Anfragen, auf deren Basis die Vector-Datenbank durchgesucht werden kann, um mehr Informationen zum Kontext im Rahmen der Anforderungen und Hintergrund des Gastes einzuholen.
Jede Anfrage soll genau eine Frage beinhalten.
Schreibe jede Anfrage hintereinande ohne Nummerierung und trenne sie dabei untereinander durch folgendes Symbol: *
Sie sollen UNBEDINGT durch folgendes Symbol getrennt werden: *
Sie dürfen KEINESWEGS nummeriert sein.
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