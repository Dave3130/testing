# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack11l111l1ll_opy_ import get_logger
logger = get_logger(__name__)
bstack11ll1l111ll_opy_: Dict[str, float] = {}
bstack11ll1l11ll1_opy_: List = []
bstack11ll11llll1_opy_ = 5
bstack111ll11lll_opy_ = os.path.join(os.getcwd(), bstack11l111_opy_ (u"ࠨ࡮ࡲ࡫ࠬᚥ"), bstack11l111_opy_ (u"ࠩ࡮ࡩࡾ࠳࡭ࡦࡶࡵ࡭ࡨࡹ࠮࡫ࡵࡲࡲࠬᚦ"))
logging.getLogger(bstack11l111_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠬᚧ")).setLevel(logging.WARNING)
lock = FileLock(bstack111ll11lll_opy_+bstack11l111_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥᚨ"))
class bstack11ll1l11l11_opy_:
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
    def __init__(self, duration: float, name: str, start_time: float, bstack11ll1l11111_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11ll1l11111_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11l111_opy_ (u"ࠧࡳࡥࡢࡵࡸࡶࡪࠨᚩ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llll11ll11_opy_:
    global bstack11ll1l111ll_opy_
    @staticmethod
    def bstack1ll11l11ll1_opy_(key: str):
        bstack1ll1l1l11l1_opy_ = bstack1llll11ll11_opy_.bstack11ll1l1l111_opy_(key)
        bstack1llll11ll11_opy_.mark(bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᚪ"))
        return bstack1ll1l1l11l1_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11ll1l111ll_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥᚫ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llll11ll11_opy_.mark(end)
            bstack1llll11ll11_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳ࠻ࠢࡾࢁࠧᚬ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11ll1l111ll_opy_ or end not in bstack11ll1l111ll_opy_:
                logger.debug(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸࡺࡡࡳࡶࠣ࡯ࡪࡿࠠࡸ࡫ࡷ࡬ࠥࡼࡡ࡭ࡷࡨࠤࢀࢃࠠࡰࡴࠣࡩࡳࡪࠠ࡬ࡧࡼࠤࡼ࡯ࡴࡩࠢࡹࡥࡱࡻࡥࠡࡽࢀࠦᚭ").format(start,end))
                return
            duration: float = bstack11ll1l111ll_opy_[end] - bstack11ll1l111ll_opy_[start]
            bstack11ll11lllll_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡌࡗࡤࡘࡕࡏࡐࡌࡒࡌࠨᚮ"), bstack11l111_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥᚯ")).lower() == bstack11l111_opy_ (u"ࠧࡺࡲࡶࡧࠥᚰ")
            bstack11ll1l1111l_opy_: bstack11ll1l11l11_opy_ = bstack11ll1l11l11_opy_(duration, label, bstack11ll1l111ll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨᚱ"), 0), command, test_name, hook_type, bstack11ll11lllll_opy_)
            del bstack11ll1l111ll_opy_[start]
            del bstack11ll1l111ll_opy_[end]
            bstack1llll11ll11_opy_.bstack11ll1l11l1l_opy_(bstack11ll1l1111l_opy_)
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡥࡢࡵࡸࡶ࡮ࡴࡧࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࡀࠠࡼࡿࠥᚲ").format(e))
    @staticmethod
    def bstack11ll1l11l1l_opy_(bstack11ll1l1111l_opy_):
        os.makedirs(os.path.dirname(bstack111ll11lll_opy_)) if not os.path.exists(os.path.dirname(bstack111ll11lll_opy_)) else None
        bstack1llll11ll11_opy_.bstack11ll1l111l1_opy_()
        try:
            with lock:
                with open(bstack111ll11lll_opy_, bstack11l111_opy_ (u"ࠣࡴ࠮ࠦᚳ"), encoding=bstack11l111_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᚴ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11ll1l1111l_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11ll1l11lll_opy_:
            logger.debug(bstack11l111_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠤࢀࢃࠢᚵ").format(bstack11ll1l11lll_opy_))
            with lock:
                with open(bstack111ll11lll_opy_, bstack11l111_opy_ (u"ࠦࡼࠨᚶ"), encoding=bstack11l111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᚷ")) as file:
                    data = [bstack11ll1l1111l_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡡࡱࡲࡨࡲࡩࠦࡻࡾࠤᚸ").format(str(e)))
        finally:
            if os.path.exists(bstack111ll11lll_opy_+bstack11l111_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᚹ")):
                os.remove(bstack111ll11lll_opy_+bstack11l111_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢᚺ"))
    @staticmethod
    def bstack11ll1l111l1_opy_():
        attempt = 0
        while (attempt < bstack11ll11llll1_opy_):
            attempt += 1
            if os.path.exists(bstack111ll11lll_opy_+bstack11l111_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣᚻ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1l1l111_opy_(label: str) -> str:
        try:
            return bstack11l111_opy_ (u"ࠥࡿࢂࡀࡻࡾࠤᚼ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11l111_opy_ (u"ࠦࡊࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᚽ").format(e))