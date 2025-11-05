# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack111111l11l_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll11l1ll1_opy_: Dict[str, float] = {}
bstack11ll11ll111_opy_: List = []
bstack11ll11ll11l_opy_ = 5
bstack1ll1111l1l_opy_ = os.path.join(os.getcwd(), bstack11111_opy_ (u"ࠨ࡮ࡲ࡫ࠬᛁ"), bstack11111_opy_ (u"ࠩ࡮ࡩࡾ࠳࡭ࡦࡶࡵ࡭ࡨࡹ࠮࡫ࡵࡲࡲࠬᛂ"))
logging.getLogger(bstack11111_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠬᛃ")).setLevel(logging.WARNING)
lock = FileLock(bstack1ll1111l1l_opy_+bstack11111_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥᛄ"))
class bstack11ll11ll1l1_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll11lll11_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll11lll11_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11111_opy_ (u"ࠧࡳࡥࡢࡵࡸࡶࡪࠨᛅ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llll1ll1l1_opy_:
    global bstack11ll11l1ll1_opy_
    @staticmethod
    def bstack1ll1111lll1_opy_(key: str):
        bstack1ll11llll1l_opy_ = bstack1llll1ll1l1_opy_.bstack11ll11lllll_opy_(key)
        bstack1llll1ll1l1_opy_.mark(bstack1ll11llll1l_opy_+bstack11111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᛆ"))
        return bstack1ll11llll1l_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll11l1ll1_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠢࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥᛇ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llll1ll1l1_opy_.mark(end)
            bstack1llll1ll1l1_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳ࠻ࠢࡾࢁࠧᛈ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll11l1ll1_opy_ or end not in bstack11ll11l1ll1_opy_:
                logger.debug(bstack11111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸࡺࡡࡳࡶࠣ࡯ࡪࡿࠠࡸ࡫ࡷ࡬ࠥࡼࡡ࡭ࡷࡨࠤࢀࢃࠠࡰࡴࠣࡩࡳࡪࠠ࡬ࡧࡼࠤࡼ࡯ࡴࡩࠢࡹࡥࡱࡻࡥࠡࡽࢀࠦᛉ").format(start,end))
                return
            duration: float = bstack11ll11l1ll1_opy_[end] - bstack11ll11l1ll1_opy_[start]
            bstack11ll11ll1ll_opy_ = os.environ.get(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡌࡗࡤࡘࡕࡏࡐࡌࡒࡌࠨᛊ"), bstack11111_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥᛋ")).lower() == bstack11111_opy_ (u"ࠧࡺࡲࡶࡧࠥᛌ")
            bstack11ll11lll1l_opy_: bstack11ll11ll1l1_opy_ = bstack11ll11ll1l1_opy_(duration, label, bstack11ll11l1ll1_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨᛍ"), 0), command, test_name, hook_type, bstack11ll11ll1ll_opy_)
            del bstack11ll11l1ll1_opy_[start]
            del bstack11ll11l1ll1_opy_[end]
            bstack1llll1ll1l1_opy_.bstack11ll11l1lll_opy_(bstack11ll11lll1l_opy_)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡥࡢࡵࡸࡶ࡮ࡴࡧࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࡀࠠࡼࡿࠥᛎ").format(e))
    @staticmethod
    def bstack11ll11l1lll_opy_(bstack11ll11lll1l_opy_):
        os.makedirs(os.path.dirname(bstack1ll1111l1l_opy_)) if not os.path.exists(os.path.dirname(bstack1ll1111l1l_opy_)) else None
        bstack1llll1ll1l1_opy_.bstack11ll11l1l1l_opy_()
        try:
            with lock:
                with open(bstack1ll1111l1l_opy_, bstack11111_opy_ (u"ࠣࡴ࠮ࠦᛏ"), encoding=bstack11111_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᛐ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll11lll1l_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll11llll1_opy_:
            logger.debug(bstack11111_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠤࢀࢃࠢᛑ").format(bstack11ll11llll1_opy_))
            with lock:
                with open(bstack1ll1111l1l_opy_, bstack11111_opy_ (u"ࠦࡼࠨᛒ"), encoding=bstack11111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᛓ")) as file:
                    data = [bstack11ll11lll1l_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡡࡱࡲࡨࡲࡩࠦࡻࡾࠤᛔ").format(str(e)))
        finally:
            if os.path.exists(bstack1ll1111l1l_opy_+bstack11111_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᛕ")):
                os.remove(bstack1ll1111l1l_opy_+bstack11111_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᛖ"))
    @staticmethod
    def bstack11ll11l1l1l_opy_():
        attempt = 0
        while (attempt < bstack11ll11ll11l_opy_):
            attempt += 1
            if os.path.exists(bstack1ll1111l1l_opy_+bstack11111_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᛗ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll11lllll_opy_(label: str) -> str:
        try:
            return bstack11111_opy_ (u"ࠥࡿࢂࡀࡻࡾࠤᛘ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠦࡊࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᛙ").format(e))