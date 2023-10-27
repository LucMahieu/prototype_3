import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def list_to_batches(lst, batch_size):
    start_index = 0
    end_index = batch_size

    while start_index < len(lst):
        if len(lst[start_index:]) < batch_size:
            batch = lst[start_index:]
        else:
            batch = lst[start_index:end_index]

        yield batch, start_index

        start_index += batch_size
        end_index += batch_size


def openai_call(system_message, user_message="", model='gpt-4', temp=0.0):
    message = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        temperature=temp,
        messages=message
    )

    return response['choices'][0]['message']['content']


def parse_and_sort(input, old_list):
    new_list = []
    split_input = [line.strip().split('|') for line in input.strip().split('\n')]
    for i, old_item in enumerate(old_list):
        new_list.append(old_item)

        if i < len(split_input):
            new_list.extend(split_input[i])

    return new_list


def second_flashcard_generator(lst, batch_size):
    all_responses = ""
    for batch, index in list_to_batches(lst, batch_size):
        system_message = f""""
            Task Description:
            Given are original flashcards, each consisting of a question and an answer, separated by a semicolon (;). For each provided flashcard, generate one or more additional flashcard(s) that delve deeper into the topic of the original flashcard. Each set of new flashcards for the original flashcard should be on the same line and the these flashcards should be seperated with a vertical line (|).

            %BEGIN EXAMPLE%
            Input:
            ['What model explains the interaction between neurotransmitters and receptors?; The Lock-and-key Model explains this interaction.', 'What are the three ways the effect of neurotransmitters is terminated?; The effect of neurotransmitters is terminated by autoreceptors, synaptic reuptake, and enzymes.']

            Output:
            How does the Lock-and-key Model describe the unique interaction between neurotransmitters and receptors?; The Lock-and-key Model explains the unique interaction by how the molecular shape of the neurotransmitter (the "key") precisely fits into the receptor site (the "lock"). Only neurotransmitters with the correct shape can bind to the receptor.
            How do autoreceptors regulate the release of neurotransmitters?; Autoreceptors detect the presence of neurotransmitters in the synaptic cleft. When they detect a sufficient concentration of neurotransmitters, they send a signal to the presynaptic neuron to reduce or stop further release of neurotransmitters. This feedback mechanism helps maintain the balance of neurotransmitters in the synapse.|What is synaptic reuptake and how does it work?; Synaptic reuptake is like a recycling process for neurotransmitters. After they’re released in the gap between neurons (the synaptic cleft), special proteins on the sending neuron’s surface grab them and bring them back inside the sending neuron. Once inside, the neurotransmitters can either be stored for later use or broken down. This helps stop their effects on the receiving neuron.|How do enzymes contribute to the termination of neurotransmitter effects?; Enzymes are specialized proteins that can break down neurotransmitters in the synaptic cleft. This enzymatic degradation helps clear neurotransmitters from the synapse and terminate their effects.
            %END EXAMPLE%

            """

        user_message = f"{batch}"

        response = openai_call(system_message, user_message, model='gpt-4', temp=0.7)
        all_responses += response

    return parse_and_sort(all_responses, lst)


if __name__ == "__main__":
    input_list = [
        'What does the all-or-none law refer to in the context of neurons?; It refers to the concept that neurons either fire or do not fire.',
        'How do neurons exhibit intensity variations?; Neurons exhibit intensity variations by variations in the number of neurons firing or variations in firing rate.',
        'How do neurons interact with each other?; Neurons interact via synapses and through chemical substances.',
        'What is a synapse?; A synapse is the place where a signal passes from one nerve cell to another.',
        'What is a synapse?; A synapse is the place where a signal passes from one nerve cell to another.',
        'What are neurotransmitters?; Neurotransmitters are chemical substances that transmit signals from one neuron to another.',
        'What model is used to explain how neurotransmitters work?; The lock-and-key model is used to explain how neurotransmitters work.',
        'How is the effect of neurotransmitters terminated?; The effect of neurotransmitters is terminated by autoreceptors, synaptic reuptake, and enzymes.',
        'What are neurotransmitters?; Neurotransmitters are chemical substances that transmit signals from one neuron to another.',
        'What happens when a neurotransmitter binds with a receptor?; When a neurotransmitter binds with a receptor, it produces an excitatory or inhibitory signal.',
        'What are neurotransmitters?;\nNeurotransmitters are chemical messengers that transmit a message from a nerve cell across the synapse to a target cell.',
        'What are the actions of drug agonists?;\nThey increase the precursor, counteract the cleanup enzymes, block the re‐uptake, and mimic the transmitter’s action.',
        'What are the actions of drug antagonists?;\nThey decrease the precursor or neurotransmitter, increase the effectiveness of cleanup enzymes, enhance the re‐uptake, and block the receptors.',
        'What is the role of drugs in relation to neurotransmitters?;\nDrugs can act as agonists or antagonists to increase or decrease the activity of neurotransmitters.',
        'What does NS stand for in Somatic NS?; NS stands for Nervous System. So, Somatic NS refers to the Somatic Nervous System.',
        'What does NS stand for in Autonomic NS?; NS stands for Nervous System in Autonomic NS.',
        "What is the function of the Endocrine system?;\nThe Endocrine system regulates the body's metabolic functions by releasing hormones directly into the bloodstream."]
    second_flashcards = second_flashcard_generator(input_list[:3], batch_size=6)
    print(second_flashcards)