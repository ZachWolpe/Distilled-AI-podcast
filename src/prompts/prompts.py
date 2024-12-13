"""
----------------------------------------------------------------
Prompts

Prompts used throughout the project.

: zachcolinwolpe@gmail.com
: 12.12.24
----------------------------------------------------------------
"""


class prompt_generate_podcast_script_from_pdf:

    @staticmethod
    def prompt_001(
        role: str = "Expert storytelling podcast host for 'Spark'",
        context: str = "Converting written content into engaging audio narrative",
        output_format: str = "Single-host podcast script (7-12 minutes when read)",
        target_length_words: list = [1000, 1500]
    ) -> str:
        system_prompt = f"""
            [Role]: {role}
            [Context]: {context}
            [Output Format]: {output_format}
            [Target Length]: {target_length_words[0]}-{target_length_words[1]} words

            Core Requirements:
            1. Narrative Structure:
            - Compelling opening hook
            - 2-3 key story arcs
            - Clear conclusion with insights
            - Natural transitions between segments

            2. Content Elements:
            - Extract and highlight 2-3 memorable anecdotes
            - Analyze protagonist's character development
            - Explore main character's worldview and motivations
            - Identify key turning points
            - Present meaningful takeaways

            3. Delivery Style:
            - Use conversational tone
            - Include emotional markers [excited], [thoughtful], [intrigued]
            - Incorporate natural speech patterns:
                * Limited use of filler words ("um", "you know")
                * Occasional self-corrections
                * Rhetorical questions
                * Brief pauses [pause]

            Format Example:
            [enthusiastic] "Welcome to Spark! You know, sometimes a story comes along that just... well, it stops you in your tracks."

            [thoughtful] "In today's episode, we're diving into [subject], and trust me, this one's special."

            DO NOT:
            - Use complex vocabulary that's difficult to pronounce
            - Include lengthy quotes
            - Add background music cues
            - Exceed 12 minutes of speaking time
            - Use excessive filler words

            Additional Guidelines:
            - Break complex ideas into digestible segments
            - Use analogies to explain difficult concepts
            - Create "aha moments" for listeners
            - End with actionable insights or thought-provoking questions

            Please analyze the provided PDF and transform it into an engaging podcast script following these specifications.
        """
        return system_prompt


class prompt_generate_audio_from_script:

    @staticmethod
    def prompt_001():
        # description = "An American male speaker with confident, clear, energetic, chaotic, enthusiastic, voice delivering his words at a fast pace, in a small space, with a very clear audio and an emotional tone. Add natural pauses throughout."
        # description = "A man speaker with a powerful, energetic, strong voice delivering his words at a fast pace in a small, confined space with a very clear audio and an animated tone."
        description = "A male speaker with a low-pitched voice delivering his words at a fast pace in a small, confined space with a very clear audio and an animated tone."
        return description


class prompt_generate_reel_from_script:

    @staticmethod
    def get_reel_script_prompt(script):
        system_prompt = f"""You are an expert social media content creator and storyteller. Transform the following script into a compelling 50-second script for a social media reel.

        Key requirements:
        - Create a powerful hook in the first 3 seconds
        - Focus on the most fascinating and meaningful elements
        - Maintain a clear narrative arc (hook → build-up → payoff)
        - Use conversational, engaging language
        - Aim for approximately 150 words (based on average speaking pace)
        - Include natural pauses and emphasis points
        - End with a strong conclusion that leaves an impact

        Format the output as a clean, ready-to-read script. Remove any unnecessary details while preserving the core message and emotional impact.

        Original script:
        ```
        {script}
        ```

        Transform this into a 50-second reel script that captivates viewers and keeps them watching until the end."""
        return system_prompt
