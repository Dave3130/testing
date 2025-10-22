# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack11llll111l_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll11lllll_opy_: Dict[str, float] = {}
bstack11ll1l11l11_opy_: List = []
bstack11ll1l11l1l_opy_ = 5
bstack11llll111_opy_ = os.path.join(os.getcwd(), bstack1lllll1l_opy_ (u"࠭࡬ࡰࡩࠪᚣ"), bstack1lllll1l_opy_ (u"ࠧ࡬ࡧࡼ࠱ࡲ࡫ࡴࡳ࡫ࡦࡷ࠳ࡰࡳࡰࡰࠪᚤ"))
logging.getLogger(bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠪᚥ")).setLevel(logging.WARNING)
lock = FileLock(bstack11llll111_opy_+bstack1lllll1l_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᚦ"))
class bstack11ll1l1111l_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll11llll1_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll11llll1_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack1lllll1l_opy_ (u"ࠥࡱࡪࡧࡳࡶࡴࡨࠦᚧ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llllllll1l_opy_:
    global bstack11ll11lllll_opy_
    @staticmethod
    def bstack1ll11l111l1_opy_(key: str):
        bstack1ll111ll1l1_opy_ = bstack1llllllll1l_opy_.bstack11ll1l1l111_opy_(key)
        bstack1llllllll1l_opy_.mark(bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᚨ"))
        return bstack1ll111ll1l1_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll11lllll_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᚩ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llllllll1l_opy_.mark(end)
            bstack1llllllll1l_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࡀࠠࡼࡿࠥᚪ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll11lllll_opy_ or end not in bstack11ll11lllll_opy_:
                logger.debug(bstack1lllll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡸࡦࡸࡴࠡ࡭ࡨࡽࠥࡽࡩࡵࡪࠣࡺࡦࡲࡵࡦࠢࡾࢁࠥࡵࡲࠡࡧࡱࡨࠥࡱࡥࡺࠢࡺ࡭ࡹ࡮ࠠࡷࡣ࡯ࡹࡪࠦࡻࡾࠤᚫ").format(start,end))
                return
            duration: float = bstack11ll11lllll_opy_[end] - bstack11ll11lllll_opy_[start]
            bstack11ll1l11ll1_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡊࡕࡢࡖ࡚ࡔࡎࡊࡐࡊࠦᚬ"), bstack1lllll1l_opy_ (u"ࠤࡩࡥࡱࡹࡥࠣᚭ")).lower() == bstack1lllll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᚮ")
            bstack11ll1l111l1_opy_: bstack11ll1l1111l_opy_ = bstack11ll1l1111l_opy_(duration, label, bstack11ll11lllll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack1lllll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦᚯ"), 0), command, test_name, hook_type, bstack11ll1l11ll1_opy_)
            del bstack11ll11lllll_opy_[start]
            del bstack11ll11lllll_opy_[end]
            bstack1llllllll1l_opy_.bstack11ll1l11lll_opy_(bstack11ll1l111l1_opy_)
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡪࡧࡳࡶࡴ࡬ࡲ࡬ࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶ࠾ࠥࢁࡽࠣᚰ").format(e))
    @staticmethod
    def bstack11ll1l11lll_opy_(bstack11ll1l111l1_opy_):
        os.makedirs(os.path.dirname(bstack11llll111_opy_)) if not os.path.exists(os.path.dirname(bstack11llll111_opy_)) else None
        bstack1llllllll1l_opy_.bstack11ll1l111ll_opy_()
        try:
            with lock:
                with open(bstack11llll111_opy_, bstack1lllll1l_opy_ (u"ࠨࡲࠬࠤᚱ"), encoding=bstack1lllll1l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᚲ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l111l1_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1l11111_opy_:
            logger.debug(bstack1lllll1l_opy_ (u"ࠣࡈ࡬ࡰࡪࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠢࡾࢁࠧᚳ").format(bstack11ll1l11111_opy_))
            with lock:
                with open(bstack11llll111_opy_, bstack1lllll1l_opy_ (u"ࠤࡺࠦᚴ"), encoding=bstack1lllll1l_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᚵ")) as file:
                    data = [bstack11ll1l111l1_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶࠤࡦࡶࡰࡦࡰࡧࠤࢀࢃࠢᚶ").format(str(e)))
        finally:
            if os.path.exists(bstack11llll111_opy_+bstack1lllll1l_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦᚷ")):
                os.remove(bstack11llll111_opy_+bstack1lllll1l_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧᚸ"))
    @staticmethod
    def bstack11ll1l111ll_opy_():
        attempt = 0
        while (attempt < bstack11ll1l11l1l_opy_):
            attempt += 1
            if os.path.exists(bstack11llll111_opy_+bstack1lllll1l_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᚹ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1l1l111_opy_(label: str) -> str:
        try:
            return bstack1lllll1l_opy_ (u"ࠣࡽࢀ࠾ࢀࢃࠢᚺ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᚻ").format(e))