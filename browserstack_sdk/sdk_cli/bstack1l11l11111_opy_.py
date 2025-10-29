# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import os
@dataclass
class bstack111l11111l_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack1l11ll111l_opy_:
    pass
class Events:
    bstack111111ll1_opy_ = bstack11ll1l_opy_ (u"ࠦࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠢሐ")
    CONNECT = bstack11ll1l_opy_ (u"ࠧࡩ࡯࡯ࡰࡨࡧࡹࠨሑ")
    bstack111lll1l1_opy_ = bstack11ll1l_opy_ (u"ࠨࡳࡩࡷࡷࡨࡴࡽ࡮ࠣሒ")
    CONFIG = bstack11ll1l_opy_ (u"ࠢࡤࡱࡱࡪ࡮࡭ࠢሓ")
    bstack1ll1l1ll1l1_opy_ = bstack11ll1l_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡷࠧሔ")
    bstack1llll1ll11_opy_ = bstack11ll1l_opy_ (u"ࠤࡨࡼ࡮ࡺࠢሕ")
class bstack1ll1l1ll111_opy_:
    bstack1ll1l1l1lll_opy_ = bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡶࡸࡦࡸࡴࡦࡦࠥሖ")
    FINISHED = bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧሗ")
class bstack1ll1l1lllll_opy_:
    bstack1ll1l1l1lll_opy_ = bstack11ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠣመ")
    FINISHED = bstack11ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࠥሙ")
class bstack1ll1l1ll1ll_opy_:
    bstack1ll1l1l1lll_opy_ = bstack11ll1l_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡶࡸࡦࡸࡴࡦࡦࠥሚ")
    FINISHED = bstack11ll1l_opy_ (u"ࠣࡪࡲࡳࡰࡥࡲࡶࡰࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧማ")
class bstack1ll1l1ll11l_opy_:
    bstack1ll1l1llll1_opy_ = bstack11ll1l_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡤࡴࡨࡥࡹ࡫ࡤࠣሜ")
class bstack1ll1l1lll1l_opy_:
    _1ll1l1lll11_opy_ = None
    def __new__(cls):
        if not cls._1ll1l1lll11_opy_:
            cls._1ll1l1lll11_opy_ = super(bstack1ll1l1lll1l_opy_, cls).__new__(cls)
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
                raise ValueError(bstack11ll1l_opy_ (u"ࠥࡇࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡳࡵࡴࡶࠣࡦࡪࠦࡣࡢ࡮࡯ࡥࡧࡲࡥࠡࡨࡲࡶࠥࠨም") + event_name)
            pid = os.getpid()
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡗ࡫ࡧࡪࡵࡷࡩࡷ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺࠠࠨࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠧࠡࡹ࡬ࡸ࡭ࠦࡰࡪࡦࠣࠦሞ") + str(pid) + bstack11ll1l_opy_ (u"ࠧࠨሟ"))
            self._hooks[event_name][pid].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            pid = os.getpid()
            callbacks = self._hooks.get(event_name, {}).get(pid, [])
            if not callbacks:
                self.logger.warning(bstack11ll1l_opy_ (u"ࠨࡎࡰࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࡷࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࠡࠩࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠨࠢࡺ࡭ࡹ࡮ࠠࡱ࡫ࡧࠤࠧሠ") + str(pid) + bstack11ll1l_opy_ (u"ࠢࠣሡ"))
                return
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡋࡱࡺࡴࡱࡩ࡯ࡩࠣࡿࡱ࡫࡮ࠩࡥࡤࡰࡱࡨࡡࡤ࡭ࡶ࠭ࢂࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࡴࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸࠥ࠭ࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠬࠦࡷࡪࡶ࡫ࠤࡵ࡯ࡤࠡࠤሢ") + str(pid) + bstack11ll1l_opy_ (u"ࠤࠥሣ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡍࡳࡼ࡯࡬ࡧࡧࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࠢࠪࡿࡪࡼࡥ࡯ࡶࡢࡲࡦࡳࡥࡾࠩࠣࡻ࡮ࡺࡨࠡࡲ࡬ࡨࠥࠨሤ") + str(pid) + bstack11ll1l_opy_ (u"ࠦࠧሥ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack11ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠫࠥࡽࡩࡵࡪࠣࡴ࡮ࡪࠠࡼࡲ࡬ࡨࢂࡀࠠࠣሦ") + str(e) + bstack11ll1l_opy_ (u"ࠨࠢሧ"))
                    traceback.print_exc()
bstack1l11l11111_opy_ = bstack1ll1l1lll1l_opy_()