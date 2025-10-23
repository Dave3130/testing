# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack11111ll111_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll1l1llll_opy_: Dict[str, float] = {}
bstack11ll1l1l111_opy_: List = []
bstack11ll1l1ll11_opy_ = 5
bstack1ll1l111l1_opy_ = os.path.join(os.getcwd(), bstack111111l_opy_ (u"ࠬࡲ࡯ࡨࠩᙸ"), bstack111111l_opy_ (u"࠭࡫ࡦࡻ࠰ࡱࡪࡺࡲࡪࡥࡶ࠲࡯ࡹ࡯࡯ࠩᙹ"))
logging.getLogger(bstack111111l_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠩᙺ")).setLevel(logging.WARNING)
lock = FileLock(bstack1ll1l111l1_opy_+bstack111111l_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᙻ"))
class bstack11ll1l1ll1l_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1ll1111_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1ll1111_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack111111l_opy_ (u"ࠤࡰࡩࡦࡹࡵࡳࡧࠥᙼ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llllll1lll_opy_:
    global bstack11ll1l1llll_opy_
    @staticmethod
    def bstack1ll1l1l11ll_opy_(key: str):
        bstack1ll1l1ll1ll_opy_ = bstack1llllll1lll_opy_.bstack11ll1ll111l_opy_(key)
        bstack1llllll1lll_opy_.mark(bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᙽ"))
        return bstack1ll1l1ll1ll_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll1l1llll_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack111111l_opy_ (u"ࠦࡊࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᙾ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llllll1lll_opy_.mark(end)
            bstack1llllll1lll_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack111111l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠ࡬ࡧࡼࠤࡲ࡫ࡴࡳ࡫ࡦࡷ࠿ࠦࡻࡾࠤᙿ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll1l1llll_opy_ or end not in bstack11ll1l1llll_opy_:
                logger.debug(bstack111111l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡷࡥࡷࡺࠠ࡬ࡧࡼࠤࡼ࡯ࡴࡩࠢࡹࡥࡱࡻࡥࠡࡽࢀࠤࡴࡸࠠࡦࡰࡧࠤࡰ࡫ࡹࠡࡹ࡬ࡸ࡭ࠦࡶࡢ࡮ࡸࡩࠥࢁࡽࠣ ").format(start,end))
                return
            duration: float = bstack11ll1l1llll_opy_[end] - bstack11ll1l1llll_opy_[start]
            bstack11ll1l1l11l_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡉࡔࡡࡕ࡙ࡓࡔࡉࡏࡉࠥᚁ"), bstack111111l_opy_ (u"ࠣࡨࡤࡰࡸ࡫ࠢᚂ")).lower() == bstack111111l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᚃ")
            bstack11ll1l1l1l1_opy_: bstack11ll1l1ll1l_opy_ = bstack11ll1l1ll1l_opy_(duration, label, bstack11ll1l1llll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack111111l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠥᚄ"), 0), command, test_name, hook_type, bstack11ll1l1l11l_opy_)
            del bstack11ll1l1llll_opy_[start]
            del bstack11ll1l1llll_opy_[end]
            bstack1llllll1lll_opy_.bstack11ll1l1lll1_opy_(bstack11ll1l1l1l1_opy_)
        except Exception as e:
            logger.debug(bstack111111l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡩࡦࡹࡵࡳ࡫ࡱ࡫ࠥࡱࡥࡺࠢࡰࡩࡹࡸࡩࡤࡵ࠽ࠤࢀࢃࠢᚅ").format(e))
    @staticmethod
    def bstack11ll1l1lll1_opy_(bstack11ll1l1l1l1_opy_):
        os.makedirs(os.path.dirname(bstack1ll1l111l1_opy_)) if not os.path.exists(os.path.dirname(bstack1ll1l111l1_opy_)) else None
        bstack1llllll1lll_opy_.bstack11ll1l11lll_opy_()
        try:
            with lock:
                with open(bstack1ll1l111l1_opy_, bstack111111l_opy_ (u"ࠧࡸࠫࠣᚆ"), encoding=bstack111111l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᚇ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l1l1l1_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1l1l1ll_opy_:
            logger.debug(bstack111111l_opy_ (u"ࠢࡇ࡫࡯ࡩࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠡࡽࢀࠦᚈ").format(bstack11ll1l1l1ll_opy_))
            with lock:
                with open(bstack1ll1l111l1_opy_, bstack111111l_opy_ (u"ࠣࡹࠥᚉ"), encoding=bstack111111l_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᚊ")) as file:
                    data = [bstack11ll1l1l1l1_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack111111l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡱࡥࡺࠢࡰࡩࡹࡸࡩࡤࡵࠣࡥࡵࡶࡥ࡯ࡦࠣࡿࢂࠨᚋ").format(str(e)))
        finally:
            if os.path.exists(bstack1ll1l111l1_opy_+bstack111111l_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥᚌ")):
                os.remove(bstack1ll1l111l1_opy_+bstack111111l_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦᚍ"))
    @staticmethod
    def bstack11ll1l11lll_opy_():
        attempt = 0
        while (attempt < bstack11ll1l1ll11_opy_):
            attempt += 1
            if os.path.exists(bstack1ll1l111l1_opy_+bstack111111l_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧᚎ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1ll111l_opy_(label: str) -> str:
        try:
            return bstack111111l_opy_ (u"ࠢࡼࡿ࠽ࡿࢂࠨᚏ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack111111l_opy_ (u"ࠣࡇࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᚐ").format(e))