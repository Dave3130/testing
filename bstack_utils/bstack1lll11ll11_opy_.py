# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack111ll1l1l_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll1l1ll11_opy_: Dict[str, float] = {}
bstack11ll1l1llll_opy_: List = []
bstack11ll1l1l11l_opy_ = 5
bstack1l1l1l11ll_opy_ = os.path.join(os.getcwd(), bstack1l_opy_ (u"ࠫࡱࡵࡧࠨᚅ"), bstack1l_opy_ (u"ࠬࡱࡥࡺ࠯ࡰࡩࡹࡸࡩࡤࡵ࠱࡮ࡸࡵ࡮ࠨᚆ"))
logging.getLogger(bstack1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠨᚇ")).setLevel(logging.WARNING)
lock = FileLock(bstack1l1l1l11ll_opy_+bstack1l_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᚈ"))
class bstack11ll1ll1111_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1ll111l_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1ll111l_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack1l_opy_ (u"ࠣ࡯ࡨࡥࡸࡻࡲࡦࠤᚉ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llll1l1lll_opy_:
    global bstack11ll1l1ll11_opy_
    @staticmethod
    def bstack1ll11llllll_opy_(key: str):
        bstack1ll1l1lll11_opy_ = bstack1llll1l1lll_opy_.bstack11ll1ll11ll_opy_(key)
        bstack1llll1l1lll_opy_.mark(bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᚊ"))
        return bstack1ll1l1lll11_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll1l1ll11_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᚋ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llll1l1lll_opy_.mark(end)
            bstack1llll1l1lll_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶ࠾ࠥࢁࡽࠣᚌ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll1l1ll11_opy_ or end not in bstack11ll1l1ll11_opy_:
                logger.debug(bstack1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡶࡤࡶࡹࠦ࡫ࡦࡻࠣࡻ࡮ࡺࡨࠡࡸࡤࡰࡺ࡫ࠠࡼࡿࠣࡳࡷࠦࡥ࡯ࡦࠣ࡯ࡪࡿࠠࡸ࡫ࡷ࡬ࠥࡼࡡ࡭ࡷࡨࠤࢀࢃࠢᚍ").format(start,end))
                return
            duration: float = bstack11ll1l1ll11_opy_[end] - bstack11ll1l1ll11_opy_[start]
            bstack11ll1l1l1ll_opy_ = os.environ.get(bstack1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡏࡓࡠࡔࡘࡒࡓࡏࡎࡈࠤᚎ"), bstack1l_opy_ (u"ࠢࡧࡣ࡯ࡷࡪࠨᚏ")).lower() == bstack1l_opy_ (u"ࠣࡶࡵࡹࡪࠨᚐ")
            bstack11ll1l1ll1l_opy_: bstack11ll1ll1111_opy_ = bstack11ll1ll1111_opy_(duration, label, bstack11ll1l1ll11_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤᚑ"), 0), command, test_name, hook_type, bstack11ll1l1l1ll_opy_)
            del bstack11ll1l1ll11_opy_[start]
            del bstack11ll1l1ll11_opy_[end]
            bstack1llll1l1lll_opy_.bstack11ll1l1lll1_opy_(bstack11ll1l1ll1l_opy_)
        except Exception as e:
            logger.debug(bstack1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡨࡥࡸࡻࡲࡪࡰࡪࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴ࠼ࠣࡿࢂࠨᚒ").format(e))
    @staticmethod
    def bstack11ll1l1lll1_opy_(bstack11ll1l1ll1l_opy_):
        os.makedirs(os.path.dirname(bstack1l1l1l11ll_opy_)) if not os.path.exists(os.path.dirname(bstack1l1l1l11ll_opy_)) else None
        bstack1llll1l1lll_opy_.bstack11ll1ll11l1_opy_()
        try:
            with lock:
                with open(bstack1l1l1l11ll_opy_, bstack1l_opy_ (u"ࠦࡷ࠱ࠢᚓ"), encoding=bstack1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᚔ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l1ll1l_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1l1l1l1_opy_:
            logger.debug(bstack1l_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠠࡼࡿࠥᚕ").format(bstack11ll1l1l1l1_opy_))
            with lock:
                with open(bstack1l1l1l11ll_opy_, bstack1l_opy_ (u"ࠢࡸࠤᚖ"), encoding=bstack1l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᚗ")) as file:
                    data = [bstack11ll1l1ll1l_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴࠢࡤࡴࡵ࡫࡮ࡥࠢࡾࢁࠧᚘ").format(str(e)))
        finally:
            if os.path.exists(bstack1l1l1l11ll_opy_+bstack1l_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤᚙ")):
                os.remove(bstack1l1l1l11ll_opy_+bstack1l_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥᚚ"))
    @staticmethod
    def bstack11ll1ll11l1_opy_():
        attempt = 0
        while (attempt < bstack11ll1l1l11l_opy_):
            attempt += 1
            if os.path.exists(bstack1l1l1l11ll_opy_+bstack1l_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦ᚛")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1ll11ll_opy_(label: str) -> str:
        try:
            return bstack1l_opy_ (u"ࠨࡻࡾ࠼ࡾࢁࠧ᚜").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥ᚝").format(e))