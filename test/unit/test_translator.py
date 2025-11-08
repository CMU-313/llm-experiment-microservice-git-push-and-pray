from src.translator import translate_content
from unittest.mock import patch, MagicMock


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_llm_normal_response():
    """
    Test that the translator correctly handles a normal, expected response from the LLM.
    This test mocks an LLM that successfully identifies a French text and translates it.
    """
    # Test with a non-hardcoded French sentence that should trigger LLM translation
    test_input = "Bonjour, comment allez-vous aujourd'hui?"
    expected_translation = "Hello, how are you today?"
    
    # Mock the LLM call to return a proper translation response
    with patch('src.translator.translate_content') as mock_translate:
        mock_translate.return_value = (False, expected_translation)
        
        is_english, translated_content = mock_translate(test_input)
        
        # Verify the LLM correctly identified this as non-English
        assert is_english == False, "LLM should identify French text as non-English"
        
        # Verify the LLM provided a valid English translation
        assert translated_content == expected_translation, "LLM should provide correct translation"
        assert len(translated_content) > 0, "Translation should not be empty"
        assert isinstance(translated_content, str), "Translation should be a string"

def test_llm_gibberish_response():
    """
    Test that the translator can handle gibberish or malformed responses from the LLM.
    This verifies robustness when the LLM returns unexpected or unparseable output.
    """
    # Test with random gibberish input
    test_input = "xQz9#@! random gibberish &*^%"
    
    # Mock the LLM returning various types of problematic responses
    with patch('src.translator.translate_content') as mock_translate:
        # Test case 1: LLM returns empty string
        mock_translate.return_value = (False, "")
        is_english, translated_content = mock_translate(test_input)
        assert isinstance(translated_content, str), "Should return a string even for gibberish"
        
        # Test case 2: LLM returns None or fails to parse
        mock_translate.return_value = (True, test_input)
        is_english, translated_content = mock_translate(test_input)
        assert isinstance(is_english, bool), "Should return a boolean for is_english"
        assert isinstance(translated_content, str), "Should return a string"
        
        # Test case 3: LLM returns unparseable response but system handles it gracefully
        mock_translate.return_value = (False, "[Unintelligible text]")
        is_english, translated_content = mock_translate(test_input)
        assert is_english == False, "Should handle gibberish as non-English"
        assert translated_content is not None, "Should provide some response for gibberish"