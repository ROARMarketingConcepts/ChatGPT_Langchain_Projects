from pydantic import BaseModel
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory

# local imports
from app.web.api import (
    get_messages_by_conversation_id,     # get messages from SQLite database
    add_message_to_conversation
)

class SQLMessageHistory(BaseChatMessageHistory, BaseModel):
    """SQL Message History."""
    
    conversation_id: str

    @property
    def messages(self):
        return get_messages_by_conversation_id(self.conversation_id)

    def add_message(self, message):
        return add_message_to_conversation(
            conversation_id=self.conversation_id, 
            role=message.type,
            content=message.content
        )
     
    def clear(): 
        pass 
    
def build_memory(chat_args):
    return ConversationBufferMemory(
        chat_memory=SQLMessageHistory(
            conversation_id=chat_args.conversation_id
            ),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
        )   
            
