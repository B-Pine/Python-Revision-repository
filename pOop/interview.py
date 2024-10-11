from fpdf import FPDF
#
# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title and font
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Interview Questions and Answers", ln=True, align='C')

# Add some space
pdf.ln(10)

# Set font for content
pdf.set_font("Arial", size=12)

# Questions and answers
qa = [
    ("What is the primary goal of the SeaChange project?",
     "The primary goal of the SeaChange project is to address ocean pollution "
     "and unsustainable fishing practices by empowering small-scale fishers "
     "through a mobile app that connects them with fair-trade buyers, "
     "provides educational resources, real-time data on fish populations, "
     "and guidance for sustainable fishing practices."),

    ("How does the SeaChange app help small-scale fishers?",
     "The SeaChange app helps small-scale fishers by connecting them with "
     "fair-trade buyers, providing educational resources, real-time data on "
     "fish populations, and offering guidance on sustainable fishing "
     "practices. This enables fishers to make informed decisions about their "
     "catch and contribute to citizen science data collection."),

    (
        "What additional activities does the SeaChange project involve apart "
        "from"
        "the mobile app?",
        "Apart from the mobile app, the SeaChange project involves mangrove "
        "restoration projects led by local youth and upcycling plastic waste "
        "into"
        "eco-friendly products through a social enterprise. These activities "
        "aim"
        "to improve fish habitats, protect coastlines, and generate income for "
        "local communities while raising awareness about plastic pollution."),

    (
        "What are the three primary goals of the SeaChange project between "
        "August 2024 and May 2025?",
        "The three primary goals between August 2024 and May 2025 are: (1) "
        "Knowledge Dissemination and Awareness, (2) Mobilization and "
        "Engagement, and (3) Legacy and Sustainability."),

    (
        "How does SeaChange plan to raise awareness about the "
        "interconnectedness of marine ecosystems and human well-being?",
        "SeaChange plans to raise awareness through targeted campaigns and "
        "dialogues with policymakers, compiling an in-depth review of the "
        "latest research on the links between seas, oceans, and human health, "
        "and disseminating this knowledge to promote understanding of marine "
        "ecosystems and human well-being."),

    ("What metrics will SeaChange use to measure progress towards its goals?",
     "SeaChange will measure progress using metrics such as the number of "
     "stakeholders engaged through mobilization activities, the reach and "
     "impact of targeted campaigns, and the adoption of ocean literacy best "
     "practices by established initiatives and networks."),

    (
        "How will SeaChange ensure the sustainability of its efforts beyond "
        "the project's duration?",
        "SeaChange will ensure sustainability by embedding best practices, "
        "codes of good conduct, and ongoing community activities. The project "
        "aims to leave a lasting legacy of ocean literacy through public "
        "campaigns and continued community engagement."),

    (
        "What role do mangrove restoration projects play in the SeaChange "
        "initiative?",
        "Mangrove restoration projects play a crucial role in improving fish "
        "habitats, protecting coastlines, and enhancing community resilience "
        "against extreme weather events. These projects are led by local "
        "youth and contribute to the overall goals of SeaChange by supporting "
        "marine ecosystems."),

    ("How does the SeaChange project address plastic pollution?",
     "The SeaChange project addresses plastic pollution by upcycling "
     "collected plastic waste into eco-friendly products through a social "
     "enterprise. This not only generates income for local communities but "
     "also raises awareness about the impact of plastic pollution on marine "
     "environments."),

    ("What inspired you to start the SeaChange project?",
     "The SeaChange project was inspired by the pressing issues of ocean "
     "pollution, unsustainable fishing practices, and the lack of resources "
     "in coastal communities. The initiative aims to combine technology, "
     "citizen science, and social entrepreneurship to create a sustainable "
     "future for marine ecosystems and coastal communities.")
]

# Add the questions and answers to the PDF
for question, answer in qa:
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(0, 10, f"Q: {question}")
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"A: {answer}")
    pdf.ln(5)

# Save the pdf with name .pdf
# file_path = "SeaChange_Interview_QA.pdf"
# pdf.output(file_path)

# # Create a new PDF document
# pdf = FPDF()

# Add a page
pdf.add_page()

# Set title and font
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Additional Interview Questions and Answers", ln=True, align='C')

# Add some space
pdf.ln(10)

# Set font for content
pdf.set_font("Arial", size=12)

# Additional Questions and answers
additional_qa = [
    ("What inspired you to start SeaChange, and how did you identify the need for such an initiative?",
     "The inspiration for SeaChange came from witnessing the detrimental effects of ocean pollution and unsustainable fishing practices on local communities and marine ecosystems. The need for such an initiative was identified through research and interaction with small-scale fishers who expressed a lack of access to fair-trade buyers, sustainable fishing practices, and educational resources."),

    ("How do you plan to scale SeaChange in the next five years?",
     "In the next five years, we plan to scale SeaChange by expanding the mobile app's user base to include more coastal communities globally, partnering with international environmental organizations, and securing additional funding to support our initiatives. We also aim to enhance our app’s features and expand our mangrove restoration and upcycling projects to more regions."),

    ("What are the biggest challenges you have faced while developing SeaChange, and how did you overcome them?",
     "One of the biggest challenges was securing initial funding and support for our project. We overcame this by creating a compelling narrative about the project’s impact, engaging with potential investors and donors, and participating in competitions like the Millennium Oceans Prize to gain visibility and credibility."),

    ("How does SeaChange ensure the reliability and accuracy of the real-time data provided to fishers?",
     "SeaChange ensures the reliability and accuracy of real-time data by collaborating with marine biologists, leveraging satellite data, and using community-based monitoring. We continuously update our data sources and employ robust data verification methods to maintain high accuracy."),

    ("Can you describe the impact of your mangrove restoration projects on local communities?",
     "Our mangrove restoration projects have had significant positive impacts on local communities by improving fish habitats, which boosts local fisheries and provides a sustainable source of income. Additionally, mangroves protect coastlines from erosion and extreme weather events, enhancing the resilience of coastal communities."),

    ("What strategies do you use to engage and mobilize local youth in your projects?",
     "We engage and mobilize local youth by involving them in hands-on activities such as mangrove planting and plastic waste collection. We also provide educational workshops, leadership training, and opportunities to participate in citizen science projects, fostering a sense of ownership and responsibility towards environmental conservation."),

    ("How do you measure the social and environmental impact of SeaChange?",
     "We measure the social and environmental impact of SeaChange through various metrics such as the number of fishers using the app, the volume of plastic waste upcycled, the area of mangroves restored, and feedback from community members. Additionally, we track changes in fish populations and coastal ecosystem health."),

    ("What partnerships have been crucial for the success of SeaChange, and how did you establish them?",
     "Crucial partnerships include collaborations with environmental NGOs, academic institutions, and government agencies. We established these partnerships through networking, presenting at environmental forums, and demonstrating the mutual benefits of working together towards common goals in ocean conservation."),

    ("What are some key features of the SeaChange app that differentiate it from other similar solutions?",
     "Key features of the SeaChange app include its real-time data on fish populations, direct connection to fair-trade buyers, educational resources on sustainable fishing practices, and a platform for citizen science contributions. The app’s holistic approach, combining technology with community engagement and environmental restoration, sets it apart from other solutions."),

    ("How do you ensure that the educational materials provided through SeaChange are accessible and relevant to small-scale fishers?",
     "We ensure accessibility and relevance by designing materials in local languages, using simple and clear visuals, and tailoring content to the specific needs and contexts of small-scale fishers. We also gather continuous feedback from users to improve and adapt the materials.")
]

# Add the additional questions and answers to the PDF
for question, answer in additional_qa:
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(0, 10, f"Q: {question}")
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"A: {answer}")
    pdf.ln(5)

# Save the pdf with name .pdf
file_path_additional = "SeaChange_Additional_Interview_QA.pdf"
pdf.output(file_path_additional)


