from dotenv import load_dotenv
import logging
import os


load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger=logging.getLogger(__name__)
REVIEWER_MODEL=os.getenv("REVIEWER_MODEL")
CRITIC_MODEL=os.getenv("CRITIC_MODEL")
BASE_URL=os.getenv("BASE_URL")
MAX_ITERATIONS=int(os.getenv("MAX_ITERATIONS"))
