# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack11l1l11ll1_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll11lll11_opy_: Dict[str, float] = {}
bstack11ll11lllll_opy_: List = []
bstack11ll11ll1ll_opy_ = 5
bstack111ll1lll1_opy_ = os.path.join(os.getcwd(), bstack11l11ll_opy_ (u"ࠧ࡭ࡱࡪࠫᚲ"), bstack11l11ll_opy_ (u"ࠨ࡭ࡨࡽ࠲ࡳࡥࡵࡴ࡬ࡧࡸ࠴ࡪࡴࡱࡱࠫᚳ"))
logging.getLogger(bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠫᚴ")).setLevel(logging.WARNING)
lock = FileLock(bstack111ll1lll1_opy_+bstack11l11ll_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤᚵ"))
class bstack11ll1l1111l_opy_:
    duration: float
    name: str
    startTime: float
    worker: int
    status: bool
    failure: str
    details: Optional[str]
    entryType: str
    platform: Optional[int]
    command: Optional[str]
    hookType: Optional[str]
    cli: Optional[bool]
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll11ll1l1_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll11ll1l1_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11l11ll_opy_ (u"ࠦࡲ࡫ࡡࡴࡷࡵࡩࠧᚶ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1lllllll1ll_opy_:
    global bstack11ll11lll11_opy_
    @staticmethod
    def bstack1ll11l111ll_opy_(key: str):
        bstack1ll11l11lll_opy_ = bstack1lllllll1ll_opy_.bstack11ll1l11l11_opy_(key)
        bstack1lllllll1ll_opy_.mark(bstack1ll11l11lll_opy_+bstack11l11ll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᚷ"))
        return bstack1ll11l11lll_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll11lll11_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11l11ll_opy_ (u"ࠨࡅࡳࡴࡲࡶ࠿ࠦࡻࡾࠤᚸ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1lllllll1ll_opy_.mark(end)
            bstack1lllllll1ll_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11l11ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹ࠺ࠡࡽࢀࠦᚹ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll11lll11_opy_ or end not in bstack11ll11lll11_opy_:
                logger.debug(bstack11l11ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡹࡧࡲࡵࠢ࡮ࡩࡾࠦࡷࡪࡶ࡫ࠤࡻࡧ࡬ࡶࡧࠣࡿࢂࠦ࡯ࡳࠢࡨࡲࡩࠦ࡫ࡦࡻࠣࡻ࡮ࡺࡨࠡࡸࡤࡰࡺ࡫ࠠࡼࡿࠥᚺ").format(start,end))
                return
            duration: float = bstack11ll11lll11_opy_[end] - bstack11ll11lll11_opy_[start]
            bstack11ll1l111ll_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡋࡖࡣࡗ࡛ࡎࡏࡋࡑࡋࠧᚻ"), bstack11l11ll_opy_ (u"ࠥࡪࡦࡲࡳࡦࠤᚼ")).lower() == bstack11l11ll_opy_ (u"ࠦࡹࡸࡵࡦࠤᚽ")
            bstack11ll11lll1l_opy_: bstack11ll1l1111l_opy_ = bstack11ll1l1111l_opy_(duration, label, bstack11ll11lll11_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11l11ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠧᚾ"), 0), command, test_name, hook_type, bstack11ll1l111ll_opy_)
            del bstack11ll11lll11_opy_[start]
            del bstack11ll11lll11_opy_[end]
            bstack1lllllll1ll_opy_.bstack11ll1l11111_opy_(bstack11ll11lll1l_opy_)
        except Exception as e:
            logger.debug(bstack11l11ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲ࡫ࡡࡴࡷࡵ࡭ࡳ࡭ࠠ࡬ࡧࡼࠤࡲ࡫ࡴࡳ࡫ࡦࡷ࠿ࠦࡻࡾࠤᚿ").format(e))
    @staticmethod
    def bstack11ll1l11111_opy_(bstack11ll11lll1l_opy_):
        os.makedirs(os.path.dirname(bstack111ll1lll1_opy_)) if not os.path.exists(os.path.dirname(bstack111ll1lll1_opy_)) else None
        bstack1lllllll1ll_opy_.bstack11ll1l111l1_opy_()
        try:
            with lock:
                with open(bstack111ll1lll1_opy_, bstack11l11ll_opy_ (u"ࠢࡳ࠭ࠥᛀ"), encoding=bstack11l11ll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᛁ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll11lll1l_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll11llll1_opy_:
            logger.debug(bstack11l11ll_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠣࡿࢂࠨᛂ").format(bstack11ll11llll1_opy_))
            with lock:
                with open(bstack111ll1lll1_opy_, bstack11l11ll_opy_ (u"ࠥࡻࠧᛃ"), encoding=bstack11l11ll_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᛄ")) as file:
                    data = [bstack11ll11lll1l_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack11l11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠ࡬ࡧࡼࠤࡲ࡫ࡴࡳ࡫ࡦࡷࠥࡧࡰࡱࡧࡱࡨࠥࢁࡽࠣᛅ").format(str(e)))
        finally:
            if os.path.exists(bstack111ll1lll1_opy_+bstack11l11ll_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧᛆ")):
                os.remove(bstack111ll1lll1_opy_+bstack11l11ll_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᛇ"))
    @staticmethod
    def bstack11ll1l111l1_opy_():
        attempt = 0
        while (attempt < bstack11ll11ll1ll_opy_):
            attempt += 1
            if os.path.exists(bstack111ll1lll1_opy_+bstack11l11ll_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᛈ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1l11l11_opy_(label: str) -> str:
        try:
            return bstack11l11ll_opy_ (u"ࠤࡾࢁ࠿ࢁࡽࠣᛉ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11l11ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᛊ").format(e))