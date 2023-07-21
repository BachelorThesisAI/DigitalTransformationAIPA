k_podcast_usage_explanation = """
# Anleitung für das Podcast-KI-Tool

**Herzlich Willkommen bei unserem Podcast-KI-Tool!** Mit dieser Anleitung führen wir Sie Schritt für Schritt durch unsere Anwendung. Entdecken Sie die einfache Planung und Durchführung eines Podcasts mit Hilfe von Künstlicher Intelligenz.

## Setup – API-Schlüssel hinterlegen

Bevor Sie mit der Planung beginnen können, müssen Sie Ihren API-Schlüssel für die KI-Funktion hinterlegen. Geben Sie den Schlüssel in das dafür vorgesehene Feld ein und klicken Sie auf "Überprüfen". Unser Tool gibt Ihnen eine Rückmeldung, ob der Schlüssel valide ist.

## Informationseingabe

In diesem Abschnitt geben Sie alle relevanten Informationen zu Ihrem Podcast ein. Hier können Sie Details zum Gast und seinem Hintergrund, mögliche SEO-Keywords, eine Kernbotschaft und Fragen, die im Podcast behandelt werden sollen, hinzufügen. Falls Sie bereits ein Thema haben, können Sie dieses hier eintragen. Falls nicht, können Sie auf der nächsten Seite eines generieren lassen. Sie können auch einen vorher erstellten Podcast-Plan hochladen, um Informationen wiederherzustellen.

## Themen-Generierung

Wenn Sie noch kein Thema für Ihren Podcast haben, hilft Ihnen unser Tool dabei, eins zu finden. Basierend auf den zuvor eingegebenen Informationen generiert das Tool Themenvorschläge. Wählen Sie das passende Thema aus und klicken Sie auf "Thema übernehmen". Das ausgewählte Thema wird automatisch in der Informationseingabe vervollständigt.

## Podcast-Planer

Der Podcast-Planer ist der zentrale Ort, an dem Sie mit der KI arbeiten. Hier laden Sie relevante Dokumente hoch, aus denen eine spezielle Datenbank erstellt wird. Anschließend lassen Sie Anfragen an diese Datenbank generieren und Antworten von der KI finden. Auf dieser Grundlage wird die Struktur Ihres Podcasts erstellt.

1. Laden Sie die relevanten Dokumente hoch.
2. Klicken Sie auf "Anfragen generieren".
3. Sie sehen nun eine Liste von Anfragen, die auf Basis Ihrer Eingaben und den hochgeladenen Dokumenten erstellt wurden. Klicken Sie auf "Datenbank abfragen".
4. Die Antworten der KI werden zusammen mit den Quellen in einer Liste angezeigt. Überprüfen Sie diese und passen Sie bei Bedarf Ihre Eingaben an und generieren Sie erneut.
5. Klicken Sie auf "Podcast-Struktur generieren".
6. Die erstellte Podcast-Struktur wird in einer Liste angezeigt. Sie können die Struktur übernehmen und für den nächsten Schritt speichern.

**Wichtig:** Nach der Generierung des Podcast-Plans können Sie diesen sowie die Informationen aus der Informationseingabe herunterladen. Falls die Seite neu geladen oder geschlossen wird, gehen diese Informationen verloren. Aufgrund technischer Einschränkungen kann die erstellte Datenbank nicht heruntergeladen werden. Sie muss nach einer Wiederherstellung erneut erstellt werden.

## Podcast-Durchführung

Auf dieser Seite führen Sie Ihren Podcast durch. Folgen Sie der zuvor generierten Podcast-Struktur und nutzen Sie die vorbereiteten Fragen und Inhalte. Mithilfe einer Transkriptionssoftware können Sie die Antworten des Gastes einfügen und sich daraus Folgefragen generieren lassen. Am Ende der Durchführung können Sie sich eine Zusammenfassung des Podcasts erstellen lassen, um Ihren Hörern einen Mehrwert zu bieten.

Viel Spaß beim Planen und Durchführen Ihres Podcasts mit unserem Tool!
"""

k_podcast_planning_general_explanation = """
In diesem Abschnitt legen Sie alle relevanten Informationen für Ihren Podcast fest. Geben Sie Details über Ihren Gast und relevante Schlüsselwörter ein, legen Sie die Kernbotschaft Ihres Podcasts fest und laden Sie Dokumente hoch, die für die Generierung des Podcast-Plans verwendet werden. Sie haben auch die Möglichkeit, ein Thema einzugeben oder es im nächsten Schritt generieren zu lassen. Zudem können Sie einen bereits erstellten Podcast-Plan hochladen, um bestehende Informationen wiederherzustellen. Nutzen Sie die Vielfalt der Möglichkeiten, um einen umfassenden und ansprechenden Podcast zu planen.
"""

k_podcast_planning_requirements_explanation = """
**Anforderungen an die Podcast-Struktur:**

Geben Sie hier Ihre spezifischen Anforderungen an die Struktur des Podcasts an. Dies kann eine Vielzahl von Elementen umfassen, und die folgenden Fragen können Ihnen dabei helfen, Ihre Gedanken zu ordnen:

- **Angestrebte Zielgruppe:** An wen richten Sie diesen Podcast hauptsächlich? Sollen es Fachleute aus einer bestimmten Branche sein, ein breiteres Publikum oder eine spezifische demografische Gruppe? Ihre Zielgruppe kann die Art der Fragen und die Diskussionstiefe beeinflussen.

*Beispiel: Dieser Podcast richtet sich hauptsächlich an junge Unternehmer, die daran interessiert sind, ihr eigenes Softwareunternehmen zu gründen.*

- **Dauer des Podcasts:** Wie lange soll Ihr Podcast dauern? Wünschen Sie sich eine kurze, prägnante Diskussion oder eine längere, tiefgreifende Konversation?

*Beispiel: Der Podcast sollte etwa 45-60 Minuten dauern.*

- **Minimale Anzahl an Fragen:** Wie viele Fragen möchten Sie mindestens stellen? Dies kann Ihnen helfen, die Länge des Podcasts und die Tiefe der Diskussion zu bestimmen.

*Beispiel: Ich möchte mindestens zehn Fragen stellen.*

- **Kernbotschaft:** Was ist die Hauptbotschaft oder das zentrale Thema, das Sie am Ende des Podcasts vermitteln möchten? Dies kann Ihnen helfen, Ihre Fragen und Diskussionen auf das zu konzentrieren, was für Sie am wichtigsten ist.

*Beispiel: Am Ende des Podcasts sollte der Zuhörer verstehen, wie wichtig Cybersicherheit ist und welche Rolle Musterfirma dabei spielt, diese Herausforderung zu meistern.*
"""

k_podcast_planning_guest_backgroundinfo_explanation = """
Bitte geben Sie hier alle relevanten Informationen zu Ihrem Gast und/oder seinem Unternehmen ein. Dies kann den Namen, die Position, das Fachgebiet, die vorherigen Erfahrungen, besondere Leistungen, Interessen, die Geschichte des Unternehmens und vieles mehr umfassen. Je mehr Details wir haben, desto besser können wir den Podcast auf Ihren Gast abstimmen.

Beispiel: Max Mustermann, CEO von Musterfirma, hat über 20 Jahre Erfahrung in der Softwareentwicklung. Musterfirma, gegründet im Jahr 2000, hat sich auf Sicherheitssoftware spezialisiert...
"""

podcast_database_creation_explanation = """
In diesem Schritt wird aus hochgeladenen Dokumenten eine Datenbank erstellt und diese werden nochmals zusammengefasst
"""

k_podcast_planning_file_upload_explanation = """
Wenn Sie zusätzliche Materialien haben, die helfen könnten, Ihren Podcast besser zu planen und zu strukturieren, laden Sie diese bitte hier hoch. Dies könnte Case Studies, theoretische Informationen zur digitalen Transformation, Pressemitteilungen, Whitepapers, Forschungsberichte oder andere relevante Dokumente umfassen, die zur weiteren Vertiefung des Themas beitragen können.

**Bitte beachten Sie, dass nur PDF-Dateien akzeptiert werden.**

Beispiel: Laden Sie hier ein Fallbeispiel hoch, in dem die digitale Transformation eines Unternehmens und seine Auswirkungen detailliert beschrieben werden.
"""

title_string = "Digital Transformation AI Podcast Planning Assistant"
general_explanation = k_podcast_planning_general_explanation
guest_backgroundinfo_explanation = k_podcast_planning_guest_backgroundinfo_explanation
guest_backgroundinfo_prompt = "Informationen über den Gast und/oder ein Unternehmen"
requirements_explanation = k_podcast_planning_requirements_explanation
requirements_prompt = "Anforderungen an Podcast-Struktur"
file_upload_explanation = k_podcast_planning_file_upload_explanation
file_upload_prompt = "PDF Dateien"
generate_button_text = "Änderungen speichern"
spinner_db_text = "Erstelle interne Dokumenten-Datenbank und fasse Dokumente zusammen"
success_db_text = "Datenbank erstellt"
spinner_generate_queries_text = "Generiere Datenbank-Anfragen"
error_generate_queries_text = "Fehler beim Generieren der Anfragen, versuchen Sie noch einmal"
success_generate_queries_text = "Anfragen generiert"
expander_queries_text = "Anfragen"
spinner_retrieve_context_text = "Frage Datenbank ab"
error_retrieve_context_text = "Kontext konnte nicht eingeholt werden"
success_retrieve_context_text = "Kontext eingeholt"
spinner_generate_podcast_structure = "Generiere Podcast-Plan"
success_generate_podcast_structure = "Podcast-Plan erstellt"