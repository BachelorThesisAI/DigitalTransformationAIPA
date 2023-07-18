k_podcast_planning_general_explanation = """
Willkommen in der Planungsphase Ihres Podcasts!
In diesem Abschnitt sammeln wir alle wichtigen Informationen, die benötigt werden, um Ihren Podcast effektiv zu planen und durchführen zu können.
Nach Hochladen der Dokumente, wird eine Datenbank erstellt.
Basierend auf Ihren Angaben zu Ziel des Podcast usw. erstellt die KI Anfragen, um Informationen aus der Datenbank einzuholen.
Mit den eingeholten Informationen kann die KI interessante Podcast-Ideen generieren
Sie können nach Bedarf die Informationen ändern und ausgewählte Schritte nochmals durchlaufen.
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
spinner_generate_podcast_structure = "Generiere Podcast-Struktur"
success_generate_podcast_structure = "Podcast-Struktur erstellt"