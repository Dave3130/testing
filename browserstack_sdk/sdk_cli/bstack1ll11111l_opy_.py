# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
from collections import defaultdict
from threading import Lock
from dataclasses import dataclass
import logging
import traceback
from typing import List, Dict, Any
import os
@dataclass
class bstack11lll1111_opy_:
    sdk_version: str
    path_config: str
    path_project: str
    test_framework: str
    frameworks: List[str]
    framework_versions: Dict[str, str]
    bs_config: Dict[str, Any]
@dataclass
class bstack111lll1l1_opy_:
    pass
class Events:
    bstack11l111ll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡣࡱࡲࡸࡸࡺࡲࡢࡲࠥᇢ")
    CONNECT = bstack1ll1ll1_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࠤᇣ")
    bstack11l11l11ll_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡶ࡬ࡺࡺࡤࡰࡹࡱࠦᇤ")
    CONFIG = bstack1ll1ll1_opy_ (u"ࠥࡧࡴࡴࡦࡪࡩࠥᇥ")
    bstack1ll1ll1ll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡳࠣᇦ")
    bstack11l11l1ll_opy_ = bstack1ll1ll1_opy_ (u"ࠧ࡫ࡸࡪࡶࠥᇧ")
class bstack1ll1ll1l1l1_opy_:
    bstack1ll1ll11ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡹࡴࡢࡴࡷࡩࡩࠨᇨ")
    FINISHED = bstack1ll1ll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣᇩ")
class bstack1ll1ll1ll11_opy_:
    bstack1ll1ll11ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡷࡹࡧࡲࡵࡧࡧࠦᇪ")
    FINISHED = bstack1ll1ll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨᇫ")
class bstack1ll1ll1l1ll_opy_:
    bstack1ll1ll11ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡹࡴࡢࡴࡷࡩࡩࠨᇬ")
    FINISHED = bstack1ll1ll1_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣᇭ")
class bstack1ll1ll1l111_opy_:
    bstack1ll1ll11lll_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡧࡷ࡫ࡡࡵࡧࡧࠦᇮ")
class bstack1ll1ll1l11l_opy_:
    _1ll1ll1lll1_opy_ = None
    def __new__(cls):
        if not cls._1ll1ll1lll1_opy_:
            cls._1ll1ll1lll1_opy_ = super(bstack1ll1ll1l11l_opy_, cls).__new__(cls)
        return cls._1ll1ll1lll1_opy_
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
                raise ValueError(bstack1ll1ll1_opy_ (u"ࠨࡃࡢ࡮࡯ࡦࡦࡩ࡫ࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡦࡥࡱࡲࡡࡣ࡮ࡨࠤ࡫ࡵࡲࠡࠤᇯ") + event_name)
            pid = os.getpid()
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡓࡧࡪ࡭ࡸࡺࡥࡳ࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࠣࠫࢀ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࡿࠪࠤࡼ࡯ࡴࡩࠢࡳ࡭ࡩࠦࠢᇰ") + str(pid) + bstack1ll1ll1_opy_ (u"ࠣࠤᇱ"))
            self._hooks[event_name][pid].append(callback)
    def invoke(self, event_name, *args, **kwargs):
        with self._lock:
            pid = os.getpid()
            callbacks = self._hooks.get(event_name, {}).get(pid, [])
            if not callbacks:
                self.logger.warning(bstack1ll1ll1_opy_ (u"ࠤࡑࡳࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࡳࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࠤࠬࢁࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࢀࠫࠥࡽࡩࡵࡪࠣࡴ࡮ࡪࠠࠣᇲ") + str(pid) + bstack1ll1ll1_opy_ (u"ࠥࠦᇳ"))
                return
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡎࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡻ࡭ࡧࡱࠬࡨࡧ࡬࡭ࡤࡤࡧࡰࡹࠩࡾࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࡷࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࠡࠩࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠨࠢࡺ࡭ࡹ࡮ࠠࡱ࡫ࡧࠤࠧᇴ") + str(pid) + bstack1ll1ll1_opy_ (u"ࠧࠨᇵ"))
            for callback in callbacks:
                try:
                    self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡉ࡯ࡸࡲ࡯ࡪࡪࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸࠥ࠭ࡻࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࢁࠬࠦࡷࡪࡶ࡫ࠤࡵ࡯ࡤࠡࠤᇶ") + str(pid) + bstack1ll1ll1_opy_ (u"ࠢࠣᇷ"))
                    callback(event_name, *args, **kwargs)
                except Exception as e:
                    self.logger.error(bstack1ll1ll1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺࠠࠨࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠧࠡࡹ࡬ࡸ࡭ࠦࡰࡪࡦࠣࡿࡵ࡯ࡤࡾ࠼ࠣࠦᇸ") + str(e) + bstack1ll1ll1_opy_ (u"ࠤࠥᇹ"))
                    traceback.print_exc()
bstack1ll11111l_opy_ = bstack1ll1ll1l11l_opy_()