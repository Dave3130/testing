# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack1l11l1lll_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll11lll11_opy_: Dict[str, float] = {}
bstack11ll1l111l1_opy_: List = []
bstack11ll1l11111_opy_ = 5
bstack1ll11l1lll_opy_ = os.path.join(os.getcwd(), bstack111l1l_opy_ (u"ࠪࡰࡴ࡭ࠧᚠ"), bstack111l1l_opy_ (u"ࠫࡰ࡫ࡹ࠮࡯ࡨࡸࡷ࡯ࡣࡴ࠰࡭ࡷࡴࡴࠧᚡ"))
logging.getLogger(bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠧᚢ")).setLevel(logging.WARNING)
lock = FileLock(bstack1ll11l1lll_opy_+bstack111l1l_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧᚣ"))
class bstack11ll11lll1l_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1l111ll_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1l111ll_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack111l1l_opy_ (u"ࠢ࡮ࡧࡤࡷࡺࡸࡥࠣᚤ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llllll11ll_opy_:
    global bstack11ll11lll11_opy_
    @staticmethod
    def bstack1ll11lllll1_opy_(key: str):
        bstack1ll11l11lll_opy_ = bstack1llllll11ll_opy_.bstack11ll1l11ll1_opy_(key)
        bstack1llllll11ll_opy_.mark(bstack1ll11l11lll_opy_+bstack111l1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᚥ"))
        return bstack1ll11l11lll_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll11lll11_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack111l1l_opy_ (u"ࠤࡈࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᚦ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llllll11ll_opy_.mark(end)
            bstack1llllll11ll_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack111l1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡱࡥࡺࠢࡰࡩࡹࡸࡩࡤࡵ࠽ࠤࢀࢃࠢᚧ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll11lll11_opy_ or end not in bstack11ll11lll11_opy_:
                logger.debug(bstack111l1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡵࡣࡵࡸࠥࡱࡥࡺࠢࡺ࡭ࡹ࡮ࠠࡷࡣ࡯ࡹࡪࠦࡻࡾࠢࡲࡶࠥ࡫࡮ࡥࠢ࡮ࡩࡾࠦࡷࡪࡶ࡫ࠤࡻࡧ࡬ࡶࡧࠣࡿࢂࠨᚨ").format(start,end))
                return
            duration: float = bstack11ll11lll11_opy_[end] - bstack11ll11lll11_opy_[start]
            bstack11ll11lllll_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡎ࡙࡟ࡓࡗࡑࡒࡎࡔࡇࠣᚩ"), bstack111l1l_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧᚪ")).lower() == bstack111l1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᚫ")
            bstack11ll1l11l1l_opy_: bstack11ll11lll1l_opy_ = bstack11ll11lll1l_opy_(duration, label, bstack11ll11lll11_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack111l1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣᚬ"), 0), command, test_name, hook_type, bstack11ll11lllll_opy_)
            del bstack11ll11lll11_opy_[start]
            del bstack11ll11lll11_opy_[end]
            bstack1llllll11ll_opy_.bstack11ll11llll1_opy_(bstack11ll1l11l1l_opy_)
        except Exception as e:
            logger.debug(bstack111l1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡧࡤࡷࡺࡸࡩ࡯ࡩࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳ࠻ࠢࡾࢁࠧᚭ").format(e))
    @staticmethod
    def bstack11ll11llll1_opy_(bstack11ll1l11l1l_opy_):
        os.makedirs(os.path.dirname(bstack1ll11l1lll_opy_)) if not os.path.exists(os.path.dirname(bstack1ll11l1lll_opy_)) else None
        bstack1llllll11ll_opy_.bstack11ll1l11l11_opy_()
        try:
            with lock:
                with open(bstack1ll11l1lll_opy_, bstack111l1l_opy_ (u"ࠥࡶ࠰ࠨᚮ"), encoding=bstack111l1l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᚯ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l11l1l_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1l1111l_opy_:
            logger.debug(bstack111l1l_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠦࡻࡾࠤᚰ").format(bstack11ll1l1111l_opy_))
            with lock:
                with open(bstack1ll11l1lll_opy_, bstack111l1l_opy_ (u"ࠨࡷࠣᚱ"), encoding=bstack111l1l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᚲ")) as file:
                    data = [bstack11ll1l11l1l_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack111l1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳࠡࡣࡳࡴࡪࡴࡤࠡࡽࢀࠦᚳ").format(str(e)))
        finally:
            if os.path.exists(bstack1ll11l1lll_opy_+bstack111l1l_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᚴ")):
                os.remove(bstack1ll11l1lll_opy_+bstack111l1l_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤᚵ"))
    @staticmethod
    def bstack11ll1l11l11_opy_():
        attempt = 0
        while (attempt < bstack11ll1l11111_opy_):
            attempt += 1
            if os.path.exists(bstack1ll11l1lll_opy_+bstack111l1l_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥᚶ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1l11ll1_opy_(label: str) -> str:
        try:
            return bstack111l1l_opy_ (u"ࠧࢁࡽ࠻ࡽࢀࠦᚷ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack111l1l_opy_ (u"ࠨࡅࡳࡴࡲࡶ࠿ࠦࡻࡾࠤᚸ").format(e))