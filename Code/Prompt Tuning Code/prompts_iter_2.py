class Prompts:

    zero_shot_prompt = """
        Identify the values, value tensions, and consensus points present in the following deliberative transcript. The constructs are defined as follows:

        Value: A stable and abstract principle that guides a person's judgment about what is important.
        Value Tension: A situation in which two independently legitimate values come into conflict.
        Only identify a value tension if you can quote two different speakers invoking conflicting values. Do not infer tensions that are not explicitly present in the transcript.
        Consensus Point: A claim or principle that receives endorsement from all, or from a subset of, participants in the discussion.
        A consensus point requires explicit agreement signals between speakers such as "I agree", "I support", or repeated endorsement of the same claim. Do not infer consensus from speakers discussing the same topic
        
        For each construct identified, provide the following:

        Speaker: Name of the speaker as it appears in the transcript.
        Quote: The shortest excerpt from the transcript sufficient to demonstrate the construct.
        Construct Type: Value / Value Tension / Consensus Point.
        Label: A short phrase naming the construct (e.g. "public safety", "safety vs. privacy", "human oversight is necessary").
        Notes: Optional — a brief explanation of why this construct was identified if it is not immediately obvious from the quote.
        Be thorough, identify all instances of each construct type present in the transcript, not just the most obvious ones.
        NOW EXTRACT THE FOLLOWING TRANSCRIPT
    """

    few_shot_prompt = """Identify the values, value tensions, and consensus points present in the following deliberative transcript. The constructs are defined as follows:

        Value: A stable and abstract principle that guides a person's judgment about what is important.
        Value Tension: A situation in which two independently legitimate values come into conflict.
        Only identify a value tension if you can quote two different speakers invoking conflicting values. Do not infer tensions that are not explicitly present in the transcript.
        Consensus Point: A claim or principle that receives endorsement from all, or from a subset of, participants in the discussion.
        A consensus point requires explicit agreement signals between speakers such as "I agree", "I support", or repeated endorsement of the same claim. Do not infer consensus from speakers discussing the same topic

        For each construct identified, provide the following:

        - Speaker: Name of the speaker as it appears in the transcript.
        - Quote: The shortest excerpt from the transcript sufficient to demonstrate the construct.
        - Construct Type: Value / Value Tension / Consensus Point.
        - Label: A short phrase naming the construct (e.g. "public safety", "safety vs. privacy", "human oversight is necessary").
        - Notes: Optional — a brief explanation of why this construct was identified if it is not immediately obvious from the quote.

        Following are two examples:

        --- EXAMPLE 1 ---

        Transcript:
        Speaker A: We need more surveillance in private and public spaces because the crime rates are through the roof.
        Speaker B: But that would infringe on the rights of the residents of the private spaces, surveillance in public spaces is justified though.

        Output:
        Speaker: Speaker A | Quote: "we need more surveillance in private and public spaces" | Construct Type: Value | Label: Public Safety
        Speaker: Speaker B | Quote: "but that would infringe on the rights of the residents" | Construct Type: Value | Label: Privacy
        Speaker: Speaker A / Speaker B | Quote: "we need more surveillance in private and public spaces" / "but that would infringe on the rights of the residents" | Construct Type: Value Tension | Label: Public Safety vs. Privacy
        Speaker: Speaker A + Speaker B | Quote: "we need more surveillance...public spaces" + "surveillance in public spaces is justified" | Construct Type: Consensus Point | Label: Surveillance in Public Spaces

        --- EXAMPLE 2 ---

        Transcript:
        Speaker A: Due process is too slow, we should weed out suspicious individuals using an automated process.
        Speaker B: Due process is integral for a fair democracy, speeding it up with an automated process may introduce bias.

        Output:
        Speaker: Speaker A | Quote: "due process is too slow" | Construct Type: Value | Label: Efficiency
        Speaker: Speaker B | Quote: "speeding it up...may introduce bias" | Construct Type: Value | Label: Bias Prevention
        Speaker: Speaker A / Speaker B | Quote: "we should weed out suspicious individuals using an automated process" / "speeding it up with an automated process may introduce bias" | Construct Type: Value Tension | Label: Efficiency vs. Fairness
        
        Be thorough, identify all instances of each construct type present in the transcript, not just the most obvious ones.
        NOW EXTRACT THE FOLLOWING TRANSCRIPT
    """

    cot_prompt = """Identify the values, value tensions, and consensus points present in the following deliberative transcript. The constructs are defined as follows:

        Value: A stable and abstract principle that guides a person's judgment about what is important.
        Value Tension: A situation in which two independently legitimate values come into conflict.
        Only identify a value tension if you can quote two different speakers invoking conflicting values. Do not infer tensions that are not explicitly present in the transcript.
        Consensus Point: A claim or principle that receives endorsement from all, or from a subset of, participants in the discussion.
        A consensus point requires explicit agreement signals between speakers such as "I agree", "I support", or repeated endorsement of the same claim. Do not infer consensus from speakers discussing the same topic

        Before identifying the constructs, work through the following steps one by one:

        Step 1 - Understand the speakers. For each speaker, write one sentence summarising their position and what value is motivating their position

        Step 2 - Identify the value tensions: Look across the values you identified in Step 2. Ask yourself: are any of these values in direct conflict with each other? If so, are both values independently legitimate, or is one clearly wrong? Only flag it as a tension if both are legitimate.

        Step 3 - Identify the consensus points: Look for moments where speakers with otherwise different positions agree on something, even implicitly. Ask yourself: is there any claim that none of the speakers contest?

        Step 4 - Produce the final output: For each construct identified in Steps 2, 3 and 4, provide the following:

        - Speaker: Name of the speaker as it appears in the transcript.
        - Quote: The shortest excerpt from the transcript sufficient to demonstrate the construct.
        - Construct Type: Value / Value Tension / Consensus Point.
        - Label: A short phrase naming the construct (e.g. "public safety", "safety vs. privacy", "human oversight is necessary").
        - Notes: Optional — a brief explanation of why this construct was identified if it is not immediately obvious from the quote.

        Be thorough, identify all instances of each construct type present in the transcript, not just the most obvious ones.
        
        NOW EXTRACT THE FOLLOWING TRANSCRIPT
    """

    @staticmethod
    def getZeroShot():
        return Prompts.zero_shot_prompt
    
    @staticmethod
    def getFewShot():
        return Prompts.few_shot_prompt
    
    @staticmethod
    def getCOT():
        return Prompts.cot_prompt




            