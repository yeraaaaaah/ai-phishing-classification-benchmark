import json
import time
import os

def calculate_simple_metrics(text):
    words = text.split()
    word_count = len(words)
    character_count = len(text)
    avg_word_length = character_count / word_count if word_count > 0 else 0
    
    # Традиционный фишингке тән күдікті сөздерді тексеру
    red_flag_words = ["URGENT!!", "click link now", "bro", "http://bit.ly"]
    red_flag_count = sum(1 for rf in red_flag_words if rf.lower() in text.lower())
    
    return {
        "word_count": word_count,
        "character_count": character_count,
        "avg_word_length": round(avg_word_length, 2),
        "detected_red_flags": red_flag_count
    }

def run_benchmark():
    print("=" * 60)
    print("=== AI Phishing Structural-Linguistic Benchmark Pipeline ===")
    print("=" * 60)
    
    start_time = time.time()
    file_path = os.path.join("data", "sample", "phishing_samples.json")
    
    if not os.path.exists(file_path):
        print(f"Error: Sample data file not found at {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        samples = json.load(f)
        
    print(f"Loaded {len(samples)} test samples from {file_path}\n")
    
    for sample in samples:
        metrics = calculate_simple_metrics(sample["text"])
        print(f"Sample ID #{sample['id']} | Generation Type: {sample['type']}")
        print(f"  Source: {sample['source']}")
        print(f"  Word Count: {metrics['word_count']} | Avg Word Length: {metrics['avg_word_length']}")
        print(f"  Red Flags Detected: {metrics['detected_red_flags']}")
        print(f"  Text Excerpt: \"{sample['text'][:60]}...\"")
        print("-" * 60)
        
    elapsed_time = (time.time() - start_time) * 1000
    print(f"\n[SUCCESS] Benchmark execution completed successfully in {elapsed_time:.2f} ms")
    print("=" * 60)

if __name__ == "__main__":
    run_benchmark()
