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
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import os
@dataclass
class bstack1l1lll1l1_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack11l11ll11l_opy_:
    pass
class Events:
    bstack111ll1llll_opy_ = bstack11l111_opy_ (u"ࠥࡦࡴࡵࡴࡴࡶࡵࡥࡵࠨᇐ")
    CONNECT = bstack11l111_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࠧᇑ")
    bstack111l111ll_opy_ = bstack11l111_opy_ (u"ࠧࡹࡨࡶࡶࡧࡳࡼࡴࠢᇒ")
    CONFIG = bstack11l111_opy_ (u"ࠨࡣࡰࡰࡩ࡭࡬ࠨᇓ")
    bstack1ll1ll111l1_opy_ = bstack11l111_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡶࠦᇔ")
    bstack11111ll1ll_opy_ = bstack11l111_opy_ (u"ࠣࡧࡻ࡭ࡹࠨᇕ")
class bstack1ll1ll1l1l1_opy_:
    bstack1ll1ll1l111_opy_ = bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡵࡷࡥࡷࡺࡥࡥࠤᇖ")
    FINISHED = bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦᇗ")
class bstack1ll1ll11ll1_opy_:
    bstack1ll1ll1l111_opy_ = bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡳࡵࡣࡵࡸࡪࡪࠢᇘ")
    FINISHED = bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤᇙ")
class bstack1ll1ll1l11l_opy_:
    bstack1ll1ll1l111_opy_ = bstack11l111_opy_ (u"ࠨࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡵࡷࡥࡷࡺࡥࡥࠤᇚ")
    FINISHED = bstack11l111_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦᇛ")
class bstack1ll1ll11l1l_opy_:
    bstack1ll1ll11l11_opy_ = bstack11l111_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡣࡳࡧࡤࡸࡪࡪࠢᇜ")
class bstack1ll1ll11lll_opy_:
    _1ll1ll111ll_opy_ = None
    def __new__(cls):
        if not cls._1ll1ll111ll_opy_:
            cls._1ll1ll111ll_opy_ = super(bstack1ll1ll11lll_opy_, cls).__new__(cls)
        return cls._1ll1ll111ll_opy_
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
                raise ValueError(bstack11l111_opy_ (u"ࠤࡆࡥࡱࡲࡢࡢࡥ࡮ࠤࡲࡻࡳࡵࠢࡥࡩࠥࡩࡡ࡭࡮ࡤࡦࡱ࡫ࠠࡧࡱࡵࠤࠧᇝ") + event_name)
            pid = os.getpid()
            self.logger.debug(bstack11l111_opy_ (u"ࠥࡖࡪ࡭ࡩࡴࡶࡨࡶ࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࠦࠧࡼࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࢂ࠭ࠠࡸ࡫ࡷ࡬ࠥࡶࡩࡥࠢࠥᇞ") + str(pid) + bstack11l111_opy_ (u"ࠦࠧᇟ"))
            self._hooks[event_name][pid].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            pid = os.getpid()
            callbacks = self._hooks.get(event_name, {}).get(pid, [])
            if not callbacks:
                self.logger.warning(bstack11l111_opy_ (u"ࠧࡔ࡯ࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࡶࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺࠠࠨࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠧࠡࡹ࡬ࡸ࡭ࠦࡰࡪࡦࠣࠦᇠ") + str(pid) + bstack11l111_opy_ (u"ࠨࠢᇡ"))
                return
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡊࡰࡹࡳࡰ࡯࡮ࡨࠢࡾࡰࡪࡴࠨࡤࡣ࡯ࡰࡧࡧࡣ࡬ࡵࠬࢁࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࡳࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠫࠥࡽࡩࡵࡪࠣࡴ࡮ࡪࠠࠣᇢ") + str(pid) + bstack11l111_opy_ (u"ࠣࠤᇣ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack11l111_opy_ (u"ࠤࡌࡲࡻࡵ࡫ࡦࡦࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࠡࠩࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠨࠢࡺ࡭ࡹ࡮ࠠࡱ࡫ࡧࠤࠧᇤ") + str(pid) + bstack11l111_opy_ (u"ࠥࠦᇥ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack11l111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࠣࠫࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠪࠤࡼ࡯ࡴࡩࠢࡳ࡭ࡩࠦࡻࡱ࡫ࡧࢁ࠿ࠦࠢᇦ") + str(e) + bstack11l111_opy_ (u"ࠧࠨᇧ"))
                    traceback.print_exc()
bstack1l1l111ll_opy_ = bstack1ll1ll11lll_opy_()