# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack11111l1ll1_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll11ll1ll_opy_: Dict[str, float] = {}
bstack11ll11ll111_opy_: List = []
bstack11ll11l1lll_opy_ = 5
bstack111l1ll11l_opy_ = os.path.join(os.getcwd(), bstack11ll1ll_opy_ (u"ࠩ࡯ࡳ࡬࠭ᛂ"), bstack11ll1ll_opy_ (u"ࠪ࡯ࡪࡿ࠭࡮ࡧࡷࡶ࡮ࡩࡳ࠯࡬ࡶࡳࡳ࠭ᛃ"))
logging.getLogger(bstack11ll1ll_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰ࠭ᛄ")).setLevel(logging.WARNING)
lock = FileLock(bstack111l1ll11l_opy_+bstack11ll1ll_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦᛅ"))
class bstack11ll11lll11_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll11lll1l_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll11lll1l_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11ll1ll_opy_ (u"ࠨ࡭ࡦࡣࡶࡹࡷ࡫ࠢᛆ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llll11l11l_opy_:
    global bstack11ll11ll1ll_opy_
    @staticmethod
    def bstack1l1lll1l111_opy_(key: str):
        bstack1l1lll1l1ll_opy_ = bstack1llll11l11l_opy_.bstack11ll11lllll_opy_(key)
        bstack1llll11l11l_opy_.mark(bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᛇ"))
        return bstack1l1lll1l1ll_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll11ll1ll_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠣࡇࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᛈ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llll11l11l_opy_.mark(end)
            bstack1llll11l11l_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴ࠼ࠣࡿࢂࠨᛉ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll11ll1ll_opy_ or end not in bstack11ll11ll1ll_opy_:
                logger.debug(bstack11ll1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡴࡢࡴࡷࠤࡰ࡫ࡹࠡࡹ࡬ࡸ࡭ࠦࡶࡢ࡮ࡸࡩࠥࢁࡽࠡࡱࡵࠤࡪࡴࡤࠡ࡭ࡨࡽࠥࡽࡩࡵࡪࠣࡺࡦࡲࡵࡦࠢࡾࢁࠧᛊ").format(start,end))
                return
            duration: float = bstack11ll11ll1ll_opy_[end] - bstack11ll11ll1ll_opy_[start]
            bstack11ll11l1ll1_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡍࡘࡥࡒࡖࡐࡑࡍࡓࡍࠢᛋ"), bstack11ll1ll_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦᛌ")).lower() == bstack11ll1ll_opy_ (u"ࠨࡴࡳࡷࡨࠦᛍ")
            bstack11ll11l1l1l_opy_: bstack11ll11lll11_opy_ = bstack11ll11lll11_opy_(duration, label, bstack11ll11ll1ll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11ll1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢᛎ"), 0), command, test_name, hook_type, bstack11ll11l1ll1_opy_)
            del bstack11ll11ll1ll_opy_[start]
            del bstack11ll11ll1ll_opy_[end]
            bstack1llll11l11l_opy_.bstack11ll11llll1_opy_(bstack11ll11l1l1l_opy_)
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡦࡣࡶࡹࡷ࡯࡮ࡨࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹ࠺ࠡࡽࢀࠦᛏ").format(e))
    @staticmethod
    def bstack11ll11llll1_opy_(bstack11ll11l1l1l_opy_):
        os.makedirs(os.path.dirname(bstack111l1ll11l_opy_)) if not os.path.exists(os.path.dirname(bstack111l1ll11l_opy_)) else None
        bstack1llll11l11l_opy_.bstack11ll11ll11l_opy_()
        try:
            with lock:
                with open(bstack111l1ll11l_opy_, bstack11ll1ll_opy_ (u"ࠤࡵ࠯ࠧᛐ"), encoding=bstack11ll1ll_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᛑ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll11l1l1l_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll11ll1l1_opy_:
            logger.debug(bstack11ll1ll_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠥࢁࡽࠣᛒ").format(bstack11ll11ll1l1_opy_))
            with lock:
                with open(bstack111l1ll11l_opy_, bstack11ll1ll_opy_ (u"ࠧࡽࠢᛓ"), encoding=bstack11ll1ll_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᛔ")) as file:
                    data = [bstack11ll11l1l1l_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡢࡲࡳࡩࡳࡪࠠࡼࡿࠥᛕ").format(str(e)))
        finally:
            if os.path.exists(bstack111l1ll11l_opy_+bstack11ll1ll_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᛖ")):
                os.remove(bstack111l1ll11l_opy_+bstack11ll1ll_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᛗ"))
    @staticmethod
    def bstack11ll11ll11l_opy_():
        attempt = 0
        while (attempt < bstack11ll11l1lll_opy_):
            attempt += 1
            if os.path.exists(bstack111l1ll11l_opy_+bstack11ll1ll_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤᛘ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll11lllll_opy_(label: str) -> str:
        try:
            return bstack11ll1ll_opy_ (u"ࠦࢀࢃ࠺ࡼࡿࠥᛙ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᛚ").format(e))