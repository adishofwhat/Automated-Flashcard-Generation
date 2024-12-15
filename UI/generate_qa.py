from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Initialize the model and tokenizer
model_path = "potsawee/t5-large-generation-squad-QuestionAnswer"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

def gen_qa(context, num_questions=5):
    """
    Generate multiple question-answer pairs from the given context.
    """
    questions_answers = []
    context_length = len(context)
    chunk_size = context_length // num_questions
    
    for i in range(num_questions):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < num_questions - 1 else context_length
        chunk = context[start_idx:end_idx]
        
        inputs = tokenizer(chunk, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=100)
        question_answer = tokenizer.decode(outputs[0], skip_special_tokens=False)
        question_answer = question_answer.replace(tokenizer.pad_token, "").replace(tokenizer.eos_token, "")
        
        if tokenizer.sep_token in question_answer:
            question, answer = question_answer.split(tokenizer.sep_token)
            questions_answers.append((question, answer))
    
    return questions_answers
