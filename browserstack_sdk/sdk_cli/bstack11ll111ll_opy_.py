# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import os
@dataclass
class bstack111lll1111_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack11lllllll1_opy_:
    pass
class Events:
    bstack11lllll11l_opy_ = bstack1l111ll_opy_ (u"ࠢࡣࡱࡲࡸࡸࡺࡲࡢࡲࠥᇾ")
    CONNECT = bstack1l111ll_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࠤᇿ")
    bstack11ll1ll111_opy_ = bstack1l111ll_opy_ (u"ࠤࡶ࡬ࡺࡺࡤࡰࡹࡱࠦሀ")
    CONFIG = bstack1l111ll_opy_ (u"ࠥࡧࡴࡴࡦࡪࡩࠥሁ")
    bstack1ll1ll11111_opy_ = bstack1l111ll_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡳࠣሂ")
    bstack11lll11l1l_opy_ = bstack1l111ll_opy_ (u"ࠧ࡫ࡸࡪࡶࠥሃ")
class bstack1ll1ll1111l_opy_:
    bstack1ll1l1ll11l_opy_ = bstack1l111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡹࡴࡢࡴࡷࡩࡩࠨሄ")
    FINISHED = bstack1l111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣህ")
class bstack1ll1l1llll1_opy_:
    bstack1ll1l1ll11l_opy_ = bstack1l111ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡷࡹࡧࡲࡵࡧࡧࠦሆ")
    FINISHED = bstack1l111ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨሇ")
class bstack1ll1l1lll1l_opy_:
    bstack1ll1l1ll11l_opy_ = bstack1l111ll_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡹࡴࡢࡴࡷࡩࡩࠨለ")
    FINISHED = bstack1l111ll_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣሉ")
class bstack1ll1l1ll1ll_opy_:
    bstack1ll1l1lllll_opy_ = bstack1l111ll_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡧࡷ࡫ࡡࡵࡧࡧࠦሊ")
class bstack1ll1l1ll1l1_opy_:
    _1ll1l1lll11_opy_ = None
    def __new__(cls):
        if not cls._1ll1l1lll11_opy_:
            cls._1ll1l1lll11_opy_ = super(bstack1ll1l1ll1l1_opy_, cls).__new__(cls)
        return cls._1ll1l1lll11_opy_
    def __init__(self):
        self._hooks = defaultdict(lambda: defaultdict(list))
        self._lock = Lock()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def clear(self):
        with self._lock:
            self._hooks = defaultdict(list)
    def register(self, event_name, callback):
        with self._lock:
            if not callable(callback):
                raise ValueError(bstack1l111ll_opy_ (u"ࠨࡃࡢ࡮࡯ࡦࡦࡩ࡫ࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡦࡥࡱࡲࡡࡣ࡮ࡨࠤ࡫ࡵࡲࠡࠤላ") + event_name)
            pid = os.getpid()
            self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡓࡧࡪ࡭ࡸࡺࡥࡳ࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࠣࠫࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠪࠤࡼ࡯ࡴࡩࠢࡳ࡭ࡩࠦࠢሌ") + str(pid) + bstack1l111ll_opy_ (u"ࠣࠤል"))
            self._hooks[event_name][pid].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            pid = os.getpid()
            callbacks = self._hooks.get(event_name, {}).get(pid, [])
            if not callbacks:
                self.logger.warning(bstack1l111ll_opy_ (u"ࠤࡑࡳࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࡳࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠫࠥࡽࡩࡵࡪࠣࡴ࡮ࡪࠠࠣሎ") + str(pid) + bstack1l111ll_opy_ (u"ࠥࠦሏ"))
                return
            self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡎࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡻ࡭ࡧࡱࠬࡨࡧ࡬࡭ࡤࡤࡧࡰࡹࠩࡾࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࡷࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࠡࠩࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠨࠢࡺ࡭ࡹ࡮ࠠࡱ࡫ࡧࠤࠧሐ") + str(pid) + bstack1l111ll_opy_ (u"ࠧࠨሑ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack1l111ll_opy_ (u"ࠨࡉ࡯ࡸࡲ࡯ࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸࠥ࠭ࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠬࠦࡷࡪࡶ࡫ࠤࡵ࡯ࡤࠡࠤሒ") + str(pid) + bstack1l111ll_opy_ (u"ࠢࠣሓ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack1l111ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺࠠࠨࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠧࠡࡹ࡬ࡸ࡭ࠦࡰࡪࡦࠣࡿࡵ࡯ࡤࡾ࠼ࠣࠦሔ") + str(e) + bstack1l111ll_opy_ (u"ࠤࠥሕ"))
                    traceback.print_exc()
bstack11ll111ll_opy_ = bstack1ll1l1ll1l1_opy_()