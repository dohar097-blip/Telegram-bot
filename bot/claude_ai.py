import anthropic
from config.settings import CLAUDE_API_KEY, CLAUDE_MODEL, CLAUDE_MAX_TOKENS
import logging

logger = logging.getLogger(__name__)


class ClaudeAI:
    def __init__(self):
        try:
            self.client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
            self.model = CLAUDE_MODEL
            self.max_tokens = CLAUDE_MAX_TOKENS
            self.conversation_history = {}
            logger.info("✅ Claude AI ইনিশিয়েলাইজ হয়েছে")
        except Exception as e:
            logger.error(f"❌ Claude AI ইনিশিয়েলাইজেশন ব্যর্থ: {e}")
            raise

    def chat(self, user_id, message, system_prompt=None):
        """
        Claude AI এর সাথে চ্যাট করুন
        
        Args:
            user_id: ব্যবহারকারীর ID
            message: ব্যবহারকারীর বার্তা
            system_prompt: কাস্টম সিস্টেম প্রম্পট (ঐচ্ছিক)
        
        Returns:
            Claude এর রেসপন্স
        """
        if system_prompt is None:
            system_prompt = "আপনি একটি সহায়ক Telegram বট যা বাংলা এবং ইংরেজিতে সাহায্য করে। বন্ধুত্বপূর্ণ এবং দরকারী উত্তর প্রদান করুন।"
        
        # কথোপকথনের ইতিহাস শুরু করুন বা চালিয়ে যান
        if user_id not in self.conversation_history:
            self.conversation_history[user_id] = []
        
        # নতুন বার্তা যোগ করুন
        self.conversation_history[user_id].append({
            "role": "user",
            "content": message
        })
        
        try:
            # Claude এ অনুরোধ পাঠান
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                system=system_prompt,
                messages=self.conversation_history[user_id]
            )
            
            # রেসপন্স সংরক্ষণ করুন
            assistant_message = response.content[0].text
            self.conversation_history[user_id].append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        
        except anthropic.APIError as e:
            error_msg = f"❌ Claude API ত্রুটি: {str(e)}"
            logger.error(error_msg)
            return error_msg
        except Exception as e:
            error_msg = f"❌ অপ্রত্যাশিত ত্রুটি: {str(e)}"
            logger.error(error_msg)
            return error_msg

    def customer_support(self, user_id, question):
        """
        গ্রাহক সেবা মোড
        """
        system_prompt = """আপনি Sonic Brand Market এর একজন নিবেদিত গ্রাহক সেবা প্রতিনিধি। 
        গ্রাহকদের সমস্যা সমাধানে সাহা���্য করুন, পেশাদার এবং বন্ধুত্বপূর্ণ থাকুন।
        যদি কোন সমস্যার সমাধান না করতে পারেন, সাহায্যের জন্য অফার করুন।"""
        
        return self.chat(user_id, question, system_prompt)

    def product_advisor(self, user_id, query):
        """
        প্রোডাক্ট পরামর্শ মোড
        """
        system_prompt = """আপনি Sonic Brand Market এর একজন পণ্য বিশেষজ্ঞ। 
        গ্রাহকদের তাদের প্রয়োজন অনুযায়ী সঠিক পণ্য খুঁজে পেতে সাহায্য করুন। 
        পণ্যের বৈশিষ্ট্য, সুবিধা এবং মূল্য সম্পর্কে তথ্য প্রদান করুন।"""
        
        return self.chat(user_id, query, system_prompt)

    def clear_history(self, user_id):
        """
        ব্যবহারকারীর কথোপকথনের ইতিহাস সাফ করুন
        """
        if user_id in self.conversation_history:
            del self.conversation_history[user_id]
            logger.info(f"✅ User {user_id} এর ইতিহাস সাফ হয়েছে")
