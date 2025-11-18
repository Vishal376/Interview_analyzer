from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_interview(text, max_length=150):
    """
    Summarize the interview or discussion.
    """
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def generate_feedback(analysis_dict):
    """
    Generate actionable feedback based on analysis.
    """
    feedback = []
    if analysis_dict['confidence_score'] < 60:
        feedback.append("Work on speaking confidently; reduce filler words.")
    if analysis_dict['filler_words_count'] > 5:
        feedback.append("Avoid filler words like 'um', 'uh', 'like'.")
    if analysis_dict['sentiment'] == "NEGATIVE":
        feedback.append("Focus on positive tone.")
    if analysis_dict['grammar_check'] > 5:
        feedback.append("Review grammar and sentence structure.")
    return feedback
