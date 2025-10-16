# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack1ll11111l1_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll1l1ll11_opy_: Dict[str, float] = {}
bstack11ll1ll11l1_opy_: List = []
bstack11ll1l1l1ll_opy_ = 5
bstack1llll11lll_opy_ = os.path.join(os.getcwd(), bstack1lllll1_opy_ (u"ࠩ࡯ࡳ࡬࠭ᚃ"), bstack1lllll1_opy_ (u"ࠪ࡯ࡪࡿ࠭࡮ࡧࡷࡶ࡮ࡩࡳ࠯࡬ࡶࡳࡳ࠭ᚄ"))
logging.getLogger(bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰ࠭ᚅ")).setLevel(logging.WARNING)
lock = FileLock(bstack1llll11lll_opy_+bstack1lllll1_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦᚆ"))
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1l1ll1l_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1l1ll1l_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack1lllll1_opy_ (u"ࠨ࡭ࡦࡣࡶࡹࡷ࡫ࠢᚇ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1lllllllll1_opy_:
    global bstack11ll1l1ll11_opy_
    @staticmethod
    def bstack1ll11111ll1_opy_(key: str):
        bstack1ll1l1l1111_opy_ = bstack1lllllllll1_opy_.bstack11ll1ll11ll_opy_(key)
        bstack1lllllllll1_opy_.mark(bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᚈ"))
        return bstack1ll1l1l1111_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll1l1ll11_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack1lllll1_opy_ (u"ࠣࡇࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᚉ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1lllllllll1_opy_.mark(end)
            bstack1lllllllll1_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack1lllll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴ࠼ࠣࡿࢂࠨᚊ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll1l1ll11_opy_ or end not in bstack11ll1l1ll11_opy_:
                logger.debug(bstack1lllll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡴࡢࡴࡷࠤࡰ࡫ࡹࠡࡹ࡬ࡸ࡭ࠦࡶࡢ࡮ࡸࡩࠥࢁࡽࠡࡱࡵࠤࡪࡴࡤࠡ࡭ࡨࡽࠥࡽࡩࡵࡪࠣࡺࡦࡲࡵࡦࠢࡾࢁࠧᚋ").format(start,end))
                return
            duration: float = bstack11ll1l1ll11_opy_[end] - bstack11ll1l1ll11_opy_[start]
            bstack11ll1ll1111_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡍࡘࡥࡒࡖࡐࡑࡍࡓࡍࠢᚌ"), bstack1lllll1_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦᚍ")).lower() == bstack1lllll1_opy_ (u"ࠨࡴࡳࡷࡨࠦᚎ")
            bstack11ll1l1l11l_opy_: bstack11ll1l1lll1_opy_ = bstack11ll1l1lll1_opy_(duration, label, bstack11ll1l1ll11_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack1lllll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢᚏ"), 0), command, test_name, hook_type, bstack11ll1ll1111_opy_)
            del bstack11ll1l1ll11_opy_[start]
            del bstack11ll1l1ll11_opy_[end]
            bstack1lllllllll1_opy_.bstack11ll1l1llll_opy_(bstack11ll1l1l11l_opy_)
        except Exception as e:
            logger.debug(bstack1lllll1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡦࡣࡶࡹࡷ࡯࡮ࡨࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹ࠺ࠡࡽࢀࠦᚐ").format(e))
    @staticmethod
    def bstack11ll1l1llll_opy_(bstack11ll1l1l11l_opy_):
        os.makedirs(os.path.dirname(bstack1llll11lll_opy_)) if not os.path.exists(os.path.dirname(bstack1llll11lll_opy_)) else None
        bstack1lllllllll1_opy_.bstack11ll1l1l1l1_opy_()
        try:
            with lock:
                with open(bstack1llll11lll_opy_, bstack1lllll1_opy_ (u"ࠤࡵ࠯ࠧᚑ"), encoding=bstack1lllll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᚒ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l1l11l_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1ll111l_opy_:
            logger.debug(bstack1lllll1_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠥࢁࡽࠣᚓ").format(bstack11ll1ll111l_opy_))
            with lock:
                with open(bstack1llll11lll_opy_, bstack1lllll1_opy_ (u"ࠧࡽࠢᚔ"), encoding=bstack1lllll1_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᚕ")) as file:
                    data = [bstack11ll1l1l11l_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack1lllll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡢࡲࡳࡩࡳࡪࠠࡼࡿࠥᚖ").format(str(e)))
        finally:
            if os.path.exists(bstack1llll11lll_opy_+bstack1lllll1_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᚗ")):
                os.remove(bstack1llll11lll_opy_+bstack1lllll1_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᚘ"))
    @staticmethod
    def bstack11ll1l1l1l1_opy_():
        attempt = 0
        while (attempt < bstack11ll1l1l1ll_opy_):
            attempt += 1
            if os.path.exists(bstack1llll11lll_opy_+bstack1lllll1_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤᚙ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1ll11ll_opy_(label: str) -> str:
        try:
            return bstack1lllll1_opy_ (u"ࠦࢀࢃ࠺ࡼࡿࠥᚚ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack1lllll1_opy_ (u"ࠧࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠣ᚛").format(e))