# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack1ll1111ll_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll1l11lll_opy_: Dict[str, float] = {}
bstack11ll1l1lll1_opy_: List = []
bstack11ll1l1l1ll_opy_ = 5
bstack1111llll11_opy_ = os.path.join(os.getcwd(), bstack11l1l11_opy_ (u"ࠨ࡮ࡲ࡫ࠬᙻ"), bstack11l1l11_opy_ (u"ࠩ࡮ࡩࡾ࠳࡭ࡦࡶࡵ࡭ࡨࡹ࠮࡫ࡵࡲࡲࠬᙼ"))
logging.getLogger(bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠬᙽ")).setLevel(logging.WARNING)
lock = FileLock(bstack1111llll11_opy_+bstack11l1l11_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥᙾ"))
class bstack11ll1l1l111_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1l1l1l1_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1l1l1l1_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11l1l11_opy_ (u"ࠧࡳࡥࡢࡵࡸࡶࡪࠨᙿ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack111111111l_opy_:
    global bstack11ll1l11lll_opy_
    @staticmethod
    def bstack1ll1111llll_opy_(key: str):
        bstack1ll11lll11l_opy_ = bstack111111111l_opy_.bstack11ll1ll111l_opy_(key)
        bstack111111111l_opy_.mark(bstack1ll11lll11l_opy_+bstack11l1l11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ "))
        return bstack1ll11lll11l_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll1l11lll_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠢࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥᚁ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack111111111l_opy_.mark(end)
            bstack111111111l_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳ࠻ࠢࡾࢁࠧᚂ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll1l11lll_opy_ or end not in bstack11ll1l11lll_opy_:
                logger.debug(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸࡺࡡࡳࡶࠣ࡯ࡪࡿࠠࡸ࡫ࡷ࡬ࠥࡼࡡ࡭ࡷࡨࠤࢀࢃࠠࡰࡴࠣࡩࡳࡪࠠ࡬ࡧࡼࠤࡼ࡯ࡴࡩࠢࡹࡥࡱࡻࡥࠡࡽࢀࠦᚃ").format(start,end))
                return
            duration: float = bstack11ll1l11lll_opy_[end] - bstack11ll1l11lll_opy_[start]
            bstack11ll1l1ll11_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡌࡗࡤࡘࡕࡏࡐࡌࡒࡌࠨᚄ"), bstack11l1l11_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥᚅ")).lower() == bstack11l1l11_opy_ (u"ࠧࡺࡲࡶࡧࠥᚆ")
            bstack11ll1l1ll1l_opy_: bstack11ll1l1l111_opy_ = bstack11ll1l1l111_opy_(duration, label, bstack11ll1l11lll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨᚇ"), 0), command, test_name, hook_type, bstack11ll1l1ll11_opy_)
            del bstack11ll1l11lll_opy_[start]
            del bstack11ll1l11lll_opy_[end]
            bstack111111111l_opy_.bstack11ll1ll1111_opy_(bstack11ll1l1ll1l_opy_)
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡥࡢࡵࡸࡶ࡮ࡴࡧࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࡀࠠࡼࡿࠥᚈ").format(e))
    @staticmethod
    def bstack11ll1ll1111_opy_(bstack11ll1l1ll1l_opy_):
        os.makedirs(os.path.dirname(bstack1111llll11_opy_)) if not os.path.exists(os.path.dirname(bstack1111llll11_opy_)) else None
        bstack111111111l_opy_.bstack11ll1l1l11l_opy_()
        try:
            with lock:
                with open(bstack1111llll11_opy_, bstack11l1l11_opy_ (u"ࠣࡴ࠮ࠦᚉ"), encoding=bstack11l1l11_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᚊ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l1ll1l_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1l1llll_opy_:
            logger.debug(bstack11l1l11_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠤࢀࢃࠢᚋ").format(bstack11ll1l1llll_opy_))
            with lock:
                with open(bstack1111llll11_opy_, bstack11l1l11_opy_ (u"ࠦࡼࠨᚌ"), encoding=bstack11l1l11_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᚍ")) as file:
                    data = [bstack11ll1l1ll1l_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡡࡱࡲࡨࡲࡩࠦࡻࡾࠤᚎ").format(str(e)))
        finally:
            if os.path.exists(bstack1111llll11_opy_+bstack11l1l11_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᚏ")):
                os.remove(bstack1111llll11_opy_+bstack11l1l11_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᚐ"))
    @staticmethod
    def bstack11ll1l1l11l_opy_():
        attempt = 0
        while (attempt < bstack11ll1l1l1ll_opy_):
            attempt += 1
            if os.path.exists(bstack1111llll11_opy_+bstack11l1l11_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᚑ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1ll111l_opy_(label: str) -> str:
        try:
            return bstack11l1l11_opy_ (u"ࠥࡿࢂࡀࡻࡾࠤᚒ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠦࡊࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᚓ").format(e))