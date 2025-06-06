from groq import Groq
import os

# Set the API key for Groq
os.environ["GROQ_API_KEY"] = "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"

# Initialize the client
client = Groq()

# Function to generate summary
def generate_summary(input_text):
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Summarize the given paragraph."
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,  # Disable streaming for simple output
        stop=None,
    )
    
    # Extract and return the summary
    return completion.choices[0].message
a="""Top Matches:
Paragraph: Propositional logic is a declarative language because its semantics is based on a truth
relation between sentences and possible worlds. It also has sufﬁcient expressive power to
deal with partial information, using disjunction and negation. Propositional logic has a third
positional language, the meaning of a sentence is a function of the meaning of its parts.
Similarity Score: 0.7127

Paragraph: The best sources for information on satisﬁability, both theoretical and practical, are the
Theory and Applications of Satisﬁability Testing, known as SAT. The idea of building agents with propositional logic can be traced back to the seminal
trary to popular supposition, the paper was concerned with the implementation of a Boolean
computers, have received little attention in AI, however.
Similarity Score: 0.6748

Paragraph: Logic programming is a technology that comes fairly close to embodying the declarative
a formal language and that problems should be solved by running inference processes on that
knowledge. The ideal is summed up in Robert Kowalski’s equation,
Algorithm = Logic + Control . been written in Prolog for legal, medical, ﬁnancial, and other domains.
Similarity Score: 0.6495

Paragraph: It can handle propositions that are known true, known false, or completely
algorithms for propositional logic include backtracking and local search methods and
can often solve large problems quickly. Bibliographical and Historical Notes
• Inference rules are patterns of sound inference that can be used to ﬁnd proofs.
Similarity Score: 0.6494

Paragraph: Each update step requires
state axioms that specify how each ﬂuent changes. • Decisions within a logical agent can be made by SAT solving: ﬁnding possible models
specifying future action sequences that reach the goal. This approach works only for
fully observable or sensorless environments. • Propositional logic does not scale to environments of unbounded size because it lacks
tionships among objects.
Similarity Score: 0.6356"""
# Main script to accept user input and generate summary
if __name__ == "__main__":
    input_text = a
    summary = generate_summary(input_text)
    print("\nSummary:\n", summary)
