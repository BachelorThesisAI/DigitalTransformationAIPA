

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

x = """
During digital transformation of my company many things changed.
We changed the way we looked at customer segments and thus changed the relationships to them. We started looking into what we offer to our clients and changed our product to make them feel better. 
"""

podcast_structure_planning_template = """
Your task is to plan a podcast structure according to the requirements specified further below.
The structure has to be written as a list of sections that the podcast will cover.
For example if the podcast has three sections, e.g. introduction, middle and end, the structure has to be written with each section in a new line and numbered as following:
1. introduction
2. middle
3. end

This is the requirements for the podcast:
{requirements}
"""