# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack11ll1l11l1_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll11lll11_opy_: Dict[str, float] = {}
bstack11ll11ll1ll_opy_: List = []
bstack11ll11l1lll_opy_ = 5
bstack111l1111ll_opy_ = os.path.join(os.getcwd(), bstack11l1111_opy_ (u"ࠨ࡮ࡲ࡫ࠬᛁ"), bstack11l1111_opy_ (u"ࠩ࡮ࡩࡾ࠳࡭ࡦࡶࡵ࡭ࡨࡹ࠮࡫ࡵࡲࡲࠬᛂ"))
logging.getLogger(bstack11l1111_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠬᛃ")).setLevel(logging.WARNING)
lock = FileLock(bstack111l1111ll_opy_+bstack11l1111_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥᛄ"))
class bstack11ll11llll1_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll11ll11l_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll11ll11l_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11l1111_opy_ (u"ࠧࡳࡥࡢࡵࡸࡶࡪࠨᛅ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llll1l1111_opy_:
    global bstack11ll11lll11_opy_
    @staticmethod
    def bstack1ll1111l111_opy_(key: str):
        bstack1l1llll111l_opy_ = bstack1llll1l1111_opy_.bstack11ll11lllll_opy_(key)
        bstack1llll1l1111_opy_.mark(bstack1l1llll111l_opy_+bstack11l1111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᛆ"))
        return bstack1l1llll111l_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll11lll11_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11l1111_opy_ (u"ࠢࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥᛇ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llll1l1111_opy_.mark(end)
            bstack1llll1l1111_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11l1111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳ࠻ࠢࡾࢁࠧᛈ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll11lll11_opy_ or end not in bstack11ll11lll11_opy_:
                logger.debug(bstack11l1111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸࡺࡡࡳࡶࠣ࡯ࡪࡿࠠࡸ࡫ࡷ࡬ࠥࡼࡡ࡭ࡷࡨࠤࢀࢃࠠࡰࡴࠣࡩࡳࡪࠠ࡬ࡧࡼࠤࡼ࡯ࡴࡩࠢࡹࡥࡱࡻࡥࠡࡽࢀࠦᛉ").format(start,end))
                return
            duration: float = bstack11ll11lll11_opy_[end] - bstack11ll11lll11_opy_[start]
            bstack11ll11ll1l1_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡌࡗࡤࡘࡕࡏࡐࡌࡒࡌࠨᛊ"), bstack11l1111_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥᛋ")).lower() == bstack11l1111_opy_ (u"ࠧࡺࡲࡶࡧࠥᛌ")
            bstack11ll11ll111_opy_: bstack11ll11llll1_opy_ = bstack11ll11llll1_opy_(duration, label, bstack11ll11lll11_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11l1111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨᛍ"), 0), command, test_name, hook_type, bstack11ll11ll1l1_opy_)
            del bstack11ll11lll11_opy_[start]
            del bstack11ll11lll11_opy_[end]
            bstack1llll1l1111_opy_.bstack11ll11lll1l_opy_(bstack11ll11ll111_opy_)
        except Exception as e:
            logger.debug(bstack11l1111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡥࡢࡵࡸࡶ࡮ࡴࡧࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࡀࠠࡼࡿࠥᛎ").format(e))
    @staticmethod
    def bstack11ll11lll1l_opy_(bstack11ll11ll111_opy_):
        os.makedirs(os.path.dirname(bstack111l1111ll_opy_)) if not os.path.exists(os.path.dirname(bstack111l1111ll_opy_)) else None
        bstack1llll1l1111_opy_.bstack11ll11l1ll1_opy_()
        try:
            with lock:
                with open(bstack111l1111ll_opy_, bstack11l1111_opy_ (u"ࠣࡴ࠮ࠦᛏ"), encoding=bstack11l1111_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᛐ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll11ll111_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll11l1l1l_opy_:
            logger.debug(bstack11l1111_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠤࢀࢃࠢᛑ").format(bstack11ll11l1l1l_opy_))
            with lock:
                with open(bstack111l1111ll_opy_, bstack11l1111_opy_ (u"ࠦࡼࠨᛒ"), encoding=bstack11l1111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᛓ")) as file:
                    data = [bstack11ll11ll111_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack11l1111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡡࡱࡲࡨࡲࡩࠦࡻࡾࠤᛔ").format(str(e)))
        finally:
            if os.path.exists(bstack111l1111ll_opy_+bstack11l1111_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᛕ")):
                os.remove(bstack111l1111ll_opy_+bstack11l1111_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᛖ"))
    @staticmethod
    def bstack11ll11l1ll1_opy_():
        attempt = 0
        while (attempt < bstack11ll11l1lll_opy_):
            attempt += 1
            if os.path.exists(bstack111l1111ll_opy_+bstack11l1111_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᛗ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll11lllll_opy_(label: str) -> str:
        try:
            return bstack11l1111_opy_ (u"ࠥࡿࢂࡀࡻࡾࠤᛘ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11l1111_opy_ (u"ࠦࡊࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᛙ").format(e))