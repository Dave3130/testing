# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import os
@dataclass
class bstack1l1l111l1l_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack1lll1l1l1l_opy_:
    pass
class Events:
    bstack11llllll1_opy_ = bstack1l1lll1_opy_ (u"ࠣࡤࡲࡳࡹࡹࡴࡳࡣࡳࠦᇜ")
    CONNECT = bstack1l1lll1_opy_ (u"ࠤࡦࡳࡳࡴࡥࡤࡶࠥᇝ")
    bstack1l111l1l11_opy_ = bstack1l1lll1_opy_ (u"ࠥࡷ࡭ࡻࡴࡥࡱࡺࡲࠧᇞ")
    CONFIG = bstack1l1lll1_opy_ (u"ࠦࡨࡵ࡮ࡧ࡫ࡪࠦᇟ")
    bstack1ll1ll11ll1_opy_ = bstack1l1lll1_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡴࠤᇠ")
    bstack1l1l1ll1l1_opy_ = bstack1l1lll1_opy_ (u"ࠨࡥࡹ࡫ࡷࠦᇡ")
class bstack1ll1ll1l111_opy_:
    bstack1ll1ll11l1l_opy_ = bstack1l1lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡳࡵࡣࡵࡸࡪࡪࠢᇢ")
    FINISHED = bstack1l1lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤᇣ")
class bstack1ll1ll11l11_opy_:
    bstack1ll1ll11l1l_opy_ = bstack1l1lll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡸࡺࡡࡳࡶࡨࡨࠧᇤ")
    FINISHED = bstack1l1lll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢᇥ")
class bstack1ll1ll1l11l_opy_:
    bstack1ll1ll11l1l_opy_ = bstack1l1lll1_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡳࡵࡣࡵࡸࡪࡪࠢᇦ")
    FINISHED = bstack1l1lll1_opy_ (u"ࠧ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤᇧ")
class bstack1ll1ll111ll_opy_:
    bstack1ll1ll11lll_opy_ = bstack1l1lll1_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧᇨ")
class bstack1ll1ll1l1ll_opy_:
    _1ll1ll1l1l1_opy_ = None
    def __new__(cls):
        if not cls._1ll1ll1l1l1_opy_:
            cls._1ll1ll1l1l1_opy_ = super(bstack1ll1ll1l1ll_opy_, cls).__new__(cls)
        return cls._1ll1ll1l1l1_opy_
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
                raise ValueError(bstack1l1lll1_opy_ (u"ࠢࡄࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡰࡹࡸࡺࠠࡣࡧࠣࡧࡦࡲ࡬ࡢࡤ࡯ࡩࠥ࡬࡯ࡳࠢࠥᇩ") + event_name)
            pid = os.getpid()
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡔࡨ࡫࡮ࡹࡴࡦࡴ࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠫࠥࡽࡩࡵࡪࠣࡴ࡮ࡪࠠࠣᇪ") + str(pid) + bstack1l1lll1_opy_ (u"ࠤࠥᇫ"))
            self._hooks[event_name][pid].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            pid = os.getpid()
            callbacks = self._hooks.get(event_name, {}).get(pid, [])
            if not callbacks:
                self.logger.warning(bstack1l1lll1_opy_ (u"ࠥࡒࡴࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࡴࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸࠥ࠭ࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠬࠦࡷࡪࡶ࡫ࠤࡵ࡯ࡤࠡࠤᇬ") + str(pid) + bstack1l1lll1_opy_ (u"ࠦࠧᇭ"))
                return
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡏ࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡼ࡮ࡨࡲ࠭ࡩࡡ࡭࡮ࡥࡥࡨࡱࡳࠪࡿࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࡸࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࠢࠪࡿࡪࡼࡥ࡯ࡶࡢࡲࡦࡳࡥࡾࠩࠣࡻ࡮ࡺࡨࠡࡲ࡬ࡨࠥࠨᇮ") + str(pid) + bstack1l1lll1_opy_ (u"ࠨࠢᇯ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡊࡰࡹࡳࡰ࡫ࡤࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࠦࠧࡼࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࢂ࠭ࠠࡸ࡫ࡷ࡬ࠥࡶࡩࡥࠢࠥᇰ") + str(pid) + bstack1l1lll1_opy_ (u"ࠣࠤᇱ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࡺࡴࡱࡩ࡯ࡩࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࠡࠩࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠨࠢࡺ࡭ࡹ࡮ࠠࡱ࡫ࡧࠤࢀࡶࡩࡥࡿ࠽ࠤࠧᇲ") + str(e) + bstack1l1lll1_opy_ (u"ࠥࠦᇳ"))
                    traceback.print_exc()
bstack1llll111ll_opy_ = bstack1ll1ll1l1ll_opy_()