# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack111ll1ll1l_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll1l1ll1l_opy_: Dict[str, float] = {}
bstack11ll1l1ll11_opy_: List = []
bstack11ll1l1l11l_opy_ = 5
bstack1l1l1l1l1l_opy_ = os.path.join(os.getcwd(), bstack11111_opy_ (u"࠭࡬ࡰࡩࠪᙲ"), bstack11111_opy_ (u"ࠧ࡬ࡧࡼ࠱ࡲ࡫ࡴࡳ࡫ࡦࡷ࠳ࡰࡳࡰࡰࠪᙳ"))
logging.getLogger(bstack11111_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠪᙴ")).setLevel(logging.WARNING)
lock = FileLock(bstack1l1l1l1l1l_opy_+bstack11111_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᙵ"))
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1l11lll_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1l11lll_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11111_opy_ (u"ࠥࡱࡪࡧࡳࡶࡴࡨࠦᙶ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack111111l11l_opy_:
    global bstack11ll1l1ll1l_opy_
    @staticmethod
    def bstack1ll1l11l1l1_opy_(key: str):
        bstack1l1lllll1ll_opy_ = bstack111111l11l_opy_.bstack11ll1ll1111_opy_(key)
        bstack111111l11l_opy_.mark(bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᙷ"))
        return bstack1l1lllll1ll_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll1l1ll1l_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᙸ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack111111l11l_opy_.mark(end)
            bstack111111l11l_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࡀࠠࡼࡿࠥᙹ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll1l1ll1l_opy_ or end not in bstack11ll1l1ll1l_opy_:
                logger.debug(bstack11111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡸࡦࡸࡴࠡ࡭ࡨࡽࠥࡽࡩࡵࡪࠣࡺࡦࡲࡵࡦࠢࡾࢁࠥࡵࡲࠡࡧࡱࡨࠥࡱࡥࡺࠢࡺ࡭ࡹ࡮ࠠࡷࡣ࡯ࡹࡪࠦࡻࡾࠤᙺ").format(start,end))
                return
            duration: float = bstack11ll1l1ll1l_opy_[end] - bstack11ll1l1ll1l_opy_[start]
            bstack11ll1l11ll1_opy_ = os.environ.get(bstack11111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡊࡕࡢࡖ࡚ࡔࡎࡊࡐࡊࠦᙻ"), bstack11111_opy_ (u"ࠤࡩࡥࡱࡹࡥࠣᙼ")).lower() == bstack11111_opy_ (u"ࠥࡸࡷࡻࡥࠣᙽ")
            bstack11ll1l1l1l1_opy_: bstack11ll1l1l111_opy_ = bstack11ll1l1l111_opy_(duration, label, bstack11ll1l1ll1l_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦᙾ"), 0), command, test_name, hook_type, bstack11ll1l11ll1_opy_)
            del bstack11ll1l1ll1l_opy_[start]
            del bstack11ll1l1ll1l_opy_[end]
            bstack111111l11l_opy_.bstack11ll1l1llll_opy_(bstack11ll1l1l1l1_opy_)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡪࡧࡳࡶࡴ࡬ࡲ࡬ࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶ࠾ࠥࢁࡽࠣᙿ").format(e))
    @staticmethod
    def bstack11ll1l1llll_opy_(bstack11ll1l1l1l1_opy_):
        os.makedirs(os.path.dirname(bstack1l1l1l1l1l_opy_)) if not os.path.exists(os.path.dirname(bstack1l1l1l1l1l_opy_)) else None
        bstack111111l11l_opy_.bstack11ll1l1l1ll_opy_()
        try:
            with lock:
                with open(bstack1l1l1l1l1l_opy_, bstack11111_opy_ (u"ࠨࡲࠬࠤ "), encoding=bstack11111_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᚁ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l1l1l1_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1l1lll1_opy_:
            logger.debug(bstack11111_opy_ (u"ࠣࡈ࡬ࡰࡪࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠢࡾࢁࠧᚂ").format(bstack11ll1l1lll1_opy_))
            with lock:
                with open(bstack1l1l1l1l1l_opy_, bstack11111_opy_ (u"ࠤࡺࠦᚃ"), encoding=bstack11111_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᚄ")) as file:
                    data = [bstack11ll1l1l1l1_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶࠤࡦࡶࡰࡦࡰࡧࠤࢀࢃࠢᚅ").format(str(e)))
        finally:
            if os.path.exists(bstack1l1l1l1l1l_opy_+bstack11111_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦᚆ")):
                os.remove(bstack1l1l1l1l1l_opy_+bstack11111_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧᚇ"))
    @staticmethod
    def bstack11ll1l1l1ll_opy_():
        attempt = 0
        while (attempt < bstack11ll1l1l11l_opy_):
            attempt += 1
            if os.path.exists(bstack1l1l1l1l1l_opy_+bstack11111_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᚈ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1ll1111_opy_(label: str) -> str:
        try:
            return bstack11111_opy_ (u"ࠣࡽࢀ࠾ࢀࢃࠢᚉ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠤࡈࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᚊ").format(e))