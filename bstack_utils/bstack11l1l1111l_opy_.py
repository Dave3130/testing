# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack111l11l1l_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll1l1llll_opy_: Dict[str, float] = {}
bstack11ll1l1ll1l_opy_: List = []
bstack11ll1l1l11l_opy_ = 5
bstack111l11l1ll_opy_ = os.path.join(os.getcwd(), bstack1l1lll1_opy_ (u"ࠫࡱࡵࡧࠨᙾ"), bstack1l1lll1_opy_ (u"ࠬࡱࡥࡺ࠯ࡰࡩࡹࡸࡩࡤࡵ࠱࡮ࡸࡵ࡮ࠨᙿ"))
logging.getLogger(bstack1l1lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠨ ")).setLevel(logging.WARNING)
lock = FileLock(bstack111l11l1ll_opy_+bstack1l1lll1_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᚁ"))
class bstack11ll1l1l1l1_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1l1l1ll_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1l1l1ll_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack1l1lll1_opy_ (u"ࠣ࡯ࡨࡥࡸࡻࡲࡦࠤᚂ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llll1ll11l_opy_:
    global bstack11ll1l1llll_opy_
    @staticmethod
    def bstack1ll1ll1111l_opy_(key: str):
        bstack1ll1l11l111_opy_ = bstack1llll1ll11l_opy_.bstack11ll1ll1111_opy_(key)
        bstack1llll1ll11l_opy_.mark(bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᚃ"))
        return bstack1ll1l11l111_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll1l1llll_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᚄ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llll1ll11l_opy_.mark(end)
            bstack1llll1ll11l_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶ࠾ࠥࢁࡽࠣᚅ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll1l1llll_opy_ or end not in bstack11ll1l1llll_opy_:
                logger.debug(bstack1l1lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡶࡤࡶࡹࠦ࡫ࡦࡻࠣࡻ࡮ࡺࡨࠡࡸࡤࡰࡺ࡫ࠠࡼࡿࠣࡳࡷࠦࡥ࡯ࡦࠣ࡯ࡪࡿࠠࡸ࡫ࡷ࡬ࠥࡼࡡ࡭ࡷࡨࠤࢀࢃࠢᚆ").format(start,end))
                return
            duration: float = bstack11ll1l1llll_opy_[end] - bstack11ll1l1llll_opy_[start]
            bstack11ll1l11ll1_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡏࡓࡠࡔࡘࡒࡓࡏࡎࡈࠤᚇ"), bstack1l1lll1_opy_ (u"ࠢࡧࡣ࡯ࡷࡪࠨᚈ")).lower() == bstack1l1lll1_opy_ (u"ࠣࡶࡵࡹࡪࠨᚉ")
            bstack11ll1l1ll11_opy_: bstack11ll1l1l1l1_opy_ = bstack11ll1l1l1l1_opy_(duration, label, bstack11ll1l1llll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack1l1lll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤᚊ"), 0), command, test_name, hook_type, bstack11ll1l11ll1_opy_)
            del bstack11ll1l1llll_opy_[start]
            del bstack11ll1l1llll_opy_[end]
            bstack1llll1ll11l_opy_.bstack11ll1l11lll_opy_(bstack11ll1l1ll11_opy_)
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡨࡥࡸࡻࡲࡪࡰࡪࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴ࠼ࠣࡿࢂࠨᚋ").format(e))
    @staticmethod
    def bstack11ll1l11lll_opy_(bstack11ll1l1ll11_opy_):
        os.makedirs(os.path.dirname(bstack111l11l1ll_opy_)) if not os.path.exists(os.path.dirname(bstack111l11l1ll_opy_)) else None
        bstack1llll1ll11l_opy_.bstack11ll1l1l111_opy_()
        try:
            with lock:
                with open(bstack111l11l1ll_opy_, bstack1l1lll1_opy_ (u"ࠦࡷ࠱ࠢᚌ"), encoding=bstack1l1lll1_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᚍ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l1ll11_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1l1lll1_opy_:
            logger.debug(bstack1l1lll1_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠠࡼࡿࠥᚎ").format(bstack11ll1l1lll1_opy_))
            with lock:
                with open(bstack111l11l1ll_opy_, bstack1l1lll1_opy_ (u"ࠢࡸࠤᚏ"), encoding=bstack1l1lll1_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᚐ")) as file:
                    data = [bstack11ll1l1ll11_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴࠢࡤࡴࡵ࡫࡮ࡥࠢࡾࢁࠧᚑ").format(str(e)))
        finally:
            if os.path.exists(bstack111l11l1ll_opy_+bstack1l1lll1_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤᚒ")):
                os.remove(bstack111l11l1ll_opy_+bstack1l1lll1_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥᚓ"))
    @staticmethod
    def bstack11ll1l1l111_opy_():
        attempt = 0
        while (attempt < bstack11ll1l1l11l_opy_):
            attempt += 1
            if os.path.exists(bstack111l11l1ll_opy_+bstack1l1lll1_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦᚔ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1ll1111_opy_(label: str) -> str:
        try:
            return bstack1l1lll1_opy_ (u"ࠨࡻࡾ࠼ࡾࢁࠧᚕ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠢࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥᚖ").format(e))