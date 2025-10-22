# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack111l11ll1l_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll11lll11_opy_: Dict[str, float] = {}
bstack11ll1l1111l_opy_: List = []
bstack11ll11lllll_opy_ = 5
bstack1111lll1l1_opy_ = os.path.join(os.getcwd(), bstack11l1l11_opy_ (u"ࠩ࡯ࡳ࡬࠭᚟"), bstack11l1l11_opy_ (u"ࠪ࡯ࡪࡿ࠭࡮ࡧࡷࡶ࡮ࡩࡳ࠯࡬ࡶࡳࡳ࠭ᚠ"))
logging.getLogger(bstack11l1l11_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰ࠭ᚡ")).setLevel(logging.WARNING)
lock = FileLock(bstack1111lll1l1_opy_+bstack11l1l11_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦᚢ"))
class bstack11ll1l111ll_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1l11l11_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1l11l11_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11l1l11_opy_ (u"ࠨ࡭ࡦࡣࡶࡹࡷ࡫ࠢᚣ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llllll1ll1_opy_:
    global bstack11ll11lll11_opy_
    @staticmethod
    def bstack1ll1l11l111_opy_(key: str):
        bstack1ll1l11llll_opy_ = bstack1llllll1ll1_opy_.bstack11ll1l11ll1_opy_(key)
        bstack1llllll1ll1_opy_.mark(bstack1ll1l11llll_opy_+bstack11l1l11_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᚤ"))
        return bstack1ll1l11llll_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll11lll11_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠣࡇࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᚥ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llllll1ll1_opy_.mark(end)
            bstack1llllll1ll1_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴ࠼ࠣࡿࢂࠨᚦ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll11lll11_opy_ or end not in bstack11ll11lll11_opy_:
                logger.debug(bstack11l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡴࡢࡴࡷࠤࡰ࡫ࡹࠡࡹ࡬ࡸ࡭ࠦࡶࡢ࡮ࡸࡩࠥࢁࡽࠡࡱࡵࠤࡪࡴࡤࠡ࡭ࡨࡽࠥࡽࡩࡵࡪࠣࡺࡦࡲࡵࡦࠢࡾࢁࠧᚧ").format(start,end))
                return
            duration: float = bstack11ll11lll11_opy_[end] - bstack11ll11lll11_opy_[start]
            bstack11ll1l111l1_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡍࡘࡥࡒࡖࡐࡑࡍࡓࡍࠢᚨ"), bstack11l1l11_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦᚩ")).lower() == bstack11l1l11_opy_ (u"ࠨࡴࡳࡷࡨࠦᚪ")
            bstack11ll1l11111_opy_: bstack11ll1l111ll_opy_ = bstack11ll1l111ll_opy_(duration, label, bstack11ll11lll11_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11l1l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢᚫ"), 0), command, test_name, hook_type, bstack11ll1l111l1_opy_)
            del bstack11ll11lll11_opy_[start]
            del bstack11ll11lll11_opy_[end]
            bstack1llllll1ll1_opy_.bstack11ll11lll1l_opy_(bstack11ll1l11111_opy_)
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡦࡣࡶࡹࡷ࡯࡮ࡨࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹ࠺ࠡࡽࢀࠦᚬ").format(e))
    @staticmethod
    def bstack11ll11lll1l_opy_(bstack11ll1l11111_opy_):
        os.makedirs(os.path.dirname(bstack1111lll1l1_opy_)) if not os.path.exists(os.path.dirname(bstack1111lll1l1_opy_)) else None
        bstack1llllll1ll1_opy_.bstack11ll1l11l1l_opy_()
        try:
            with lock:
                with open(bstack1111lll1l1_opy_, bstack11l1l11_opy_ (u"ࠤࡵ࠯ࠧᚭ"), encoding=bstack11l1l11_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᚮ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l11111_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll11llll1_opy_:
            logger.debug(bstack11l1l11_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠥࢁࡽࠣᚯ").format(bstack11ll11llll1_opy_))
            with lock:
                with open(bstack1111lll1l1_opy_, bstack11l1l11_opy_ (u"ࠧࡽࠢᚰ"), encoding=bstack11l1l11_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᚱ")) as file:
                    data = [bstack11ll1l11111_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡢࡲࡳࡩࡳࡪࠠࡼࡿࠥᚲ").format(str(e)))
        finally:
            if os.path.exists(bstack1111lll1l1_opy_+bstack11l1l11_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᚳ")):
                os.remove(bstack1111lll1l1_opy_+bstack11l1l11_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᚴ"))
    @staticmethod
    def bstack11ll1l11l1l_opy_():
        attempt = 0
        while (attempt < bstack11ll11lllll_opy_):
            attempt += 1
            if os.path.exists(bstack1111lll1l1_opy_+bstack11l1l11_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤᚵ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1l11ll1_opy_(label: str) -> str:
        try:
            return bstack11l1l11_opy_ (u"ࠦࢀࢃ࠺ࡼࡿࠥᚶ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᚷ").format(e))