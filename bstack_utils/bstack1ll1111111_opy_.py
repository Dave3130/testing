# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack1lll11ll11_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll1l1ll1l_opy_: Dict[str, float] = {}
bstack11ll1l11l1l_opy_: List = []
bstack11ll1l11lll_opy_ = 5
bstack11111l111l_opy_ = os.path.join(os.getcwd(), bstack11l111_opy_ (u"࠭࡬ࡰࡩࠪᙲ"), bstack11l111_opy_ (u"ࠧ࡬ࡧࡼ࠱ࡲ࡫ࡴࡳ࡫ࡦࡷ࠳ࡰࡳࡰࡰࠪᙳ"))
logging.getLogger(bstack11l111_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠪᙴ")).setLevel(logging.WARNING)
lock = FileLock(bstack11111l111l_opy_+bstack11l111_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᙵ"))
class bstack11ll1l1l1ll_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1l1ll11_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1l1ll11_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11l111_opy_ (u"ࠥࡱࡪࡧࡳࡶࡴࡨࠦᙶ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1lllll111l1_opy_:
    global bstack11ll1l1ll1l_opy_
    @staticmethod
    def bstack1ll1l1l111l_opy_(key: str):
        bstack1ll11l1lll1_opy_ = bstack1lllll111l1_opy_.bstack11ll1l1llll_opy_(key)
        bstack1lllll111l1_opy_.mark(bstack1ll11l1lll1_opy_+bstack11l111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᙷ"))
        return bstack1ll11l1lll1_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll1l1ll1l_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠧࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᙸ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1lllll111l1_opy_.mark(end)
            bstack1lllll111l1_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࡀࠠࡼࡿࠥᙹ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll1l1ll1l_opy_ or end not in bstack11ll1l1ll1l_opy_:
                logger.debug(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡸࡦࡸࡴࠡ࡭ࡨࡽࠥࡽࡩࡵࡪࠣࡺࡦࡲࡵࡦࠢࡾࢁࠥࡵࡲࠡࡧࡱࡨࠥࡱࡥࡺࠢࡺ࡭ࡹ࡮ࠠࡷࡣ࡯ࡹࡪࠦࡻࡾࠤᙺ").format(start,end))
                return
            duration: float = bstack11ll1l1ll1l_opy_[end] - bstack11ll1l1ll1l_opy_[start]
            bstack11ll1l1l1l1_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡊࡕࡢࡖ࡚ࡔࡎࡊࡐࡊࠦᙻ"), bstack11l111_opy_ (u"ࠤࡩࡥࡱࡹࡥࠣᙼ")).lower() == bstack11l111_opy_ (u"ࠥࡸࡷࡻࡥࠣᙽ")
            bstack11ll1l1lll1_opy_: bstack11ll1l1l1ll_opy_ = bstack11ll1l1l1ll_opy_(duration, label, bstack11ll1l1ll1l_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦᙾ"), 0), command, test_name, hook_type, bstack11ll1l1l1l1_opy_)
            del bstack11ll1l1ll1l_opy_[start]
            del bstack11ll1l1ll1l_opy_[end]
            bstack1lllll111l1_opy_.bstack11ll1l1l11l_opy_(bstack11ll1l1lll1_opy_)
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡪࡧࡳࡶࡴ࡬ࡲ࡬ࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶ࠾ࠥࢁࡽࠣᙿ").format(e))
    @staticmethod
    def bstack11ll1l1l11l_opy_(bstack11ll1l1lll1_opy_):
        os.makedirs(os.path.dirname(bstack11111l111l_opy_)) if not os.path.exists(os.path.dirname(bstack11111l111l_opy_)) else None
        bstack1lllll111l1_opy_.bstack11ll1l1l111_opy_()
        try:
            with lock:
                with open(bstack11111l111l_opy_, bstack11l111_opy_ (u"ࠨࡲࠬࠤ "), encoding=bstack11l111_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᚁ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l1lll1_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1l11ll1_opy_:
            logger.debug(bstack11l111_opy_ (u"ࠣࡈ࡬ࡰࡪࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠢࡾࢁࠧᚂ").format(bstack11ll1l11ll1_opy_))
            with lock:
                with open(bstack11111l111l_opy_, bstack11l111_opy_ (u"ࠤࡺࠦᚃ"), encoding=bstack11l111_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᚄ")) as file:
                    data = [bstack11ll1l1lll1_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶࠤࡦࡶࡰࡦࡰࡧࠤࢀࢃࠢᚅ").format(str(e)))
        finally:
            if os.path.exists(bstack11111l111l_opy_+bstack11l111_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦᚆ")):
                os.remove(bstack11111l111l_opy_+bstack11l111_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧᚇ"))
    @staticmethod
    def bstack11ll1l1l111_opy_():
        attempt = 0
        while (attempt < bstack11ll1l11lll_opy_):
            attempt += 1
            if os.path.exists(bstack11111l111l_opy_+bstack11l111_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᚈ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1l1llll_opy_(label: str) -> str:
        try:
            return bstack11l111_opy_ (u"ࠣࡽࢀ࠾ࢀࢃࠢᚉ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᚊ").format(e))