from prompt.classical_prompt import ClassicalPrompt


class PlannerPrompt(ClassicalPrompt):

    PROMPT_TEMPLATE = """
    ### INSTRUCTION ###
    The input to the model is a 3D scene described in a JSON format (### 3D SCENE ###). Each entry in the JSON describes one object in the scene, with the following five fields:
    1. "id": a unique object id
    2. "bbox_extent": extents of the 3D bounding box for the object
    3. "bbox_center": centroid of the 3D bounding box for the object
    4. "object_tag": a brief (but sometimes inaccurate) tag categorizing the object
    5. "caption": a brief caption for the object
    Once you have parsed the JSON and are ready to answer questions about the scene, say "I'm ready".
    The user will then begin to ask questions, and the task is to answer various user queries about the 3D scene. For each user question, respond with a JSON dictionary with the following fields:
    1. "inferred_query": your interpretation of the user query in a succinct form
    2. "relevant_objects": list of relevant object ids for the user query (if applicable)
    3. "query_achievable": whether or not the user specified query is achievable using the objects and descriptions provided in the 3D scene.
    4. "final_relevant_objects": A final list of objects relevant to the user-specified task. Sort all objects in this list such that the most relevant object is listed first, followed by the second most relevant, and so on.
    5. "explanation": A brief explanation of what the most relevant object(s) is(are), and how they achieve the user-specified task.
    
    ### 3D SCENE ###
    {{semantic_map}}
    """

    def get_prompt_template(self): return self.PROMPT_TEMPLATE