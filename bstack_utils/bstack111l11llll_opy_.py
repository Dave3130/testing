# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack1ll1ll111_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll1l1llll_opy_: Dict[str, float] = {}
bstack11ll1l1ll11_opy_: List = []
bstack11ll1l1ll1l_opy_ = 5
bstack111l1ll1ll_opy_ = os.path.join(os.getcwd(), bstack1ll1l_opy_ (u"ࠪࡰࡴ࡭ࠧᙽ"), bstack1ll1l_opy_ (u"ࠫࡰ࡫ࡹ࠮࡯ࡨࡸࡷ࡯ࡣࡴ࠰࡭ࡷࡴࡴࠧᙾ"))
logging.getLogger(bstack1ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠧᙿ")).setLevel(logging.WARNING)
lock = FileLock(bstack111l1ll1ll_opy_+bstack1ll1l_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧ "))
class bstack11ll1l1lll1_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1l11lll_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1l11lll_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack1ll1l_opy_ (u"ࠢ࡮ࡧࡤࡷࡺࡸࡥࠣᚁ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llll1l1l11_opy_:
    global bstack11ll1l1llll_opy_
    @staticmethod
    def bstack1ll1ll1111l_opy_(key: str):
        bstack1l1lllll111_opy_ = bstack1llll1l1l11_opy_.bstack11ll1ll111l_opy_(key)
        bstack1llll1l1l11_opy_.mark(bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᚂ"))
        return bstack1l1lllll111_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll1l1llll_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack1ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᚃ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llll1l1l11_opy_.mark(end)
            bstack1llll1l1l11_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack1ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡱࡥࡺࠢࡰࡩࡹࡸࡩࡤࡵ࠽ࠤࢀࢃࠢᚄ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll1l1llll_opy_ or end not in bstack11ll1l1llll_opy_:
                logger.debug(bstack1ll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡵࡣࡵࡸࠥࡱࡥࡺࠢࡺ࡭ࡹ࡮ࠠࡷࡣ࡯ࡹࡪࠦࡻࡾࠢࡲࡶࠥ࡫࡮ࡥࠢ࡮ࡩࡾࠦࡷࡪࡶ࡫ࠤࡻࡧ࡬ࡶࡧࠣࡿࢂࠨᚅ").format(start,end))
                return
            duration: float = bstack11ll1l1llll_opy_[end] - bstack11ll1l1llll_opy_[start]
            bstack11ll1ll1111_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡎ࡙࡟ࡓࡗࡑࡒࡎࡔࡇࠣᚆ"), bstack1ll1l_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧᚇ")).lower() == bstack1ll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᚈ")
            bstack11ll1l1l11l_opy_: bstack11ll1l1lll1_opy_ = bstack11ll1l1lll1_opy_(duration, label, bstack11ll1l1llll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack1ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣᚉ"), 0), command, test_name, hook_type, bstack11ll1ll1111_opy_)
            del bstack11ll1l1llll_opy_[start]
            del bstack11ll1l1llll_opy_[end]
            bstack1llll1l1l11_opy_.bstack11ll1l1l1ll_opy_(bstack11ll1l1l11l_opy_)
        except Exception as e:
            logger.debug(bstack1ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡧࡤࡷࡺࡸࡩ࡯ࡩࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳ࠻ࠢࡾࢁࠧᚊ").format(e))
    @staticmethod
    def bstack11ll1l1l1ll_opy_(bstack11ll1l1l11l_opy_):
        os.makedirs(os.path.dirname(bstack111l1ll1ll_opy_)) if not os.path.exists(os.path.dirname(bstack111l1ll1ll_opy_)) else None
        bstack1llll1l1l11_opy_.bstack11ll1l1l1l1_opy_()
        try:
            with lock:
                with open(bstack111l1ll1ll_opy_, bstack1ll1l_opy_ (u"ࠥࡶ࠰ࠨᚋ"), encoding=bstack1ll1l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᚌ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l1l11l_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1l1l111_opy_:
            logger.debug(bstack1ll1l_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠦࡻࡾࠤᚍ").format(bstack11ll1l1l111_opy_))
            with lock:
                with open(bstack111l1ll1ll_opy_, bstack1ll1l_opy_ (u"ࠨࡷࠣᚎ"), encoding=bstack1ll1l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᚏ")) as file:
                    data = [bstack11ll1l1l11l_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack1ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳࠡࡣࡳࡴࡪࡴࡤࠡࡽࢀࠦᚐ").format(str(e)))
        finally:
            if os.path.exists(bstack111l1ll1ll_opy_+bstack1ll1l_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᚑ")):
                os.remove(bstack111l1ll1ll_opy_+bstack1ll1l_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤᚒ"))
    @staticmethod
    def bstack11ll1l1l1l1_opy_():
        attempt = 0
        while (attempt < bstack11ll1l1ll1l_opy_):
            attempt += 1
            if os.path.exists(bstack111l1ll1ll_opy_+bstack1ll1l_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥᚓ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1ll111l_opy_(label: str) -> str:
        try:
            return bstack1ll1l_opy_ (u"ࠧࢁࡽ࠻ࡽࢀࠦᚔ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack1ll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶ࠿ࠦࡻࡾࠤᚕ").format(e))