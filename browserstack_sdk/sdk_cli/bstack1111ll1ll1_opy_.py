# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import os
@dataclass
class bstack11l1llll1l_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack1111l11ll1_opy_:
    pass
class Events:
    bstack11llll11l1_opy_ = bstack11l11l1_opy_ (u"ࠨࡢࡰࡱࡷࡷࡹࡸࡡࡱࠤᇶ")
    CONNECT = bstack11l11l1_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࠣᇷ")
    bstack11l11ll1l_opy_ = bstack11l11l1_opy_ (u"ࠣࡵ࡫ࡹࡹࡪ࡯ࡸࡰࠥᇸ")
    CONFIG = bstack11l11l1_opy_ (u"ࠤࡦࡳࡳ࡬ࡩࡨࠤᇹ")
    bstack1ll1ll11l1l_opy_ = bstack11l11l1_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡹࠢᇺ")
    bstack11111l11l_opy_ = bstack11l11l1_opy_ (u"ࠦࡪࡾࡩࡵࠤᇻ")
class bstack1ll1l1llll1_opy_:
    bstack1ll1l1lll1l_opy_ = bstack11l11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡸࡺࡡࡳࡶࡨࡨࠧᇼ")
    FINISHED = bstack11l11l1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᇽ")
class bstack1ll1ll111ll_opy_:
    bstack1ll1l1lll1l_opy_ = bstack11l11l1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡶࡸࡦࡸࡴࡦࡦࠥᇾ")
    FINISHED = bstack11l11l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧᇿ")
class bstack1ll1ll1111l_opy_:
    bstack1ll1l1lll1l_opy_ = bstack11l11l1_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡸࡺࡡࡳࡶࡨࡨࠧሀ")
    FINISHED = bstack11l11l1_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢሁ")
class bstack1ll1ll11l11_opy_:
    bstack1ll1l1lllll_opy_ = bstack11l11l1_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡦࡶࡪࡧࡴࡦࡦࠥሂ")
class bstack1ll1ll111l1_opy_:
    _1ll1ll11111_opy_ = None
    def __new__(cls):
        if not cls._1ll1ll11111_opy_:
            cls._1ll1ll11111_opy_ = super(bstack1ll1ll111l1_opy_, cls).__new__(cls)
        return cls._1ll1ll11111_opy_
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
                raise ValueError(bstack11l11l1_opy_ (u"ࠧࡉࡡ࡭࡮ࡥࡥࡨࡱࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡥࡤࡰࡱࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࠣሃ") + event_name)
            pid = os.getpid()
            self.logger.debug(bstack11l11l1_opy_ (u"ࠨࡒࡦࡩ࡬ࡷࡹ࡫ࡲࡪࡰࡪࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࠢࠪࡿࡪࡼࡥ࡯ࡶࡢࡲࡦࡳࡥࡾࠩࠣࡻ࡮ࡺࡨࠡࡲ࡬ࡨࠥࠨሄ") + str(pid) + bstack11l11l1_opy_ (u"ࠢࠣህ"))
            self._hooks[event_name][pid].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            pid = os.getpid()
            callbacks = self._hooks.get(event_name, {}).get(pid, [])
            if not callbacks:
                self.logger.warning(bstack11l11l1_opy_ (u"ࠣࡐࡲࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡹࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࠣࠫࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠪࠤࡼ࡯ࡴࡩࠢࡳ࡭ࡩࠦࠢሆ") + str(pid) + bstack11l11l1_opy_ (u"ࠤࠥሇ"))
                return
            self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡍࡳࡼ࡯࡬࡫ࡱ࡫ࠥࢁ࡬ࡦࡰࠫࡧࡦࡲ࡬ࡣࡣࡦ࡯ࡸ࠯ࡽࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࡶࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺࠠࠨࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠧࠡࡹ࡬ࡸ࡭ࠦࡰࡪࡦࠣࠦለ") + str(pid) + bstack11l11l1_opy_ (u"ࠦࠧሉ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡏ࡮ࡷࡱ࡮ࡩࡩࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠫࠥࡽࡩࡵࡪࠣࡴ࡮ࡪࠠࠣሊ") + str(pid) + bstack11l11l1_opy_ (u"ࠨࠢላ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack11l11l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࠦࠧࡼࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࢂ࠭ࠠࡸ࡫ࡷ࡬ࠥࡶࡩࡥࠢࡾࡴ࡮ࡪࡽ࠻ࠢࠥሌ") + str(e) + bstack11l11l1_opy_ (u"ࠣࠤል"))
                    traceback.print_exc()
bstack1111ll1ll1_opy_ = bstack1ll1ll111l1_opy_()