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
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack11l111l1_opy_
from browserstack_sdk.bstack111l1lll_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l11ll1_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack1llllllll_opy_
from bstack_utils.constants import bstack1llll111l_opy_
from bstack_utils.bstack1lllll111_opy_ import bstack111l11l1_opy_
class bstack1111l1l1_opy_:
    def __init__(self, args, logger, bstack1lllll11l_opy_, bstack11l1l11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lllll11l_opy_ = bstack1lllll11l_opy_
        self.bstack11l1l11l_opy_ = bstack11l1l11l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11l111ll_opy_ = []
        self.bstack11l11l11_opy_ = []
        self.bstack1lllll1l1_opy_ = []
        self.bstack1llll11ll_opy_ = self.bstack1111l11l_opy_()
        self.bstack1111111l_opy_ = -1
    def bstack111l1111_opy_(self, bstack11l11111_opy_):
        self.parse_args()
        self.bstack1llllll11_opy_()
        self.bstack11111111_opy_(bstack11l11111_opy_)
        self.bstack1111llll_opy_()
    def bstack1llllll1l_opy_(self):
        bstack1lllll111_opy_ = bstack111l11l1_opy_.bstack111ll1ll_opy_(self.bstack1lllll11l_opy_, self.logger)
        if bstack1lllll111_opy_ is None:
            self.logger.warn(bstack11l111_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡩࡣࡱࡨࡱ࡫ࡲࠡ࡫ࡶࠤࡳࡵࡴࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡩ࠴ࠠࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥ঒"))
            return
        bstack1lll1ll1l_opy_ = False
        bstack1lllll111_opy_.bstack1llll1111_opy_(bstack11l111_opy_ (u"ࠣࡧࡱࡥࡧࡲࡥࡥࠤও"), bstack1lllll111_opy_.bstack1llll1lll_opy_())
        start_time = time.time()
        if bstack1lllll111_opy_.bstack1llll1lll_opy_():
            test_files = self.bstack1llll1l11_opy_()
            bstack1lll1ll1l_opy_ = True
            bstack1111ll1l_opy_ = bstack1lllll111_opy_.bstack11111lll_opy_(test_files)
            if bstack1111ll1l_opy_:
                self.bstack11l111ll_opy_ = [os.path.normpath(item).replace(bstack11l111_opy_ (u"ࠩ࡟ࡠࠬঔ"), bstack11l111_opy_ (u"ࠪ࠳ࠬক")) for item in bstack1111ll1l_opy_]
                self.__1lllll1ll_opy_()
                bstack1lllll111_opy_.bstack111llll1_opy_(bstack1lll1ll1l_opy_)
                self.logger.info(bstack11l111_opy_ (u"࡙ࠦ࡫ࡳࡵࡵࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡵࡴ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤখ").format(self.bstack11l111ll_opy_))
            else:
                self.logger.info(bstack11l111_opy_ (u"ࠧࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡥࡳࡧࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡢࡺࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥগ"))
        bstack1lllll111_opy_.bstack1llll1111_opy_(bstack11l111_opy_ (u"ࠨࡴࡪ࡯ࡨࡘࡦࡱࡥ࡯ࡖࡲࡅࡵࡶ࡬ࡺࠤঘ"), int((time.time() - start_time) * 1000)) # bstack1llll1l1l_opy_ to bstack111lllll_opy_
    def __1lllll1ll_opy_(self):
        bstack11l111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡹࡥ࡭ࡨ࠱ࡷࡵ࡫ࡣࡠࡨ࡬ࡰࡪࡹࠬࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡤࡰࡱࠦ࡮ࡰࡦࡨ࡭ࡩࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦঙ")
        bstack11111ll1_opy_ = []
        try:
            from bstack111lll11_opy_.plugin import bstack1llll11l1_opy_
            results = bstack1llll11l1_opy_(bstack1111lll1_opy_=self.bstack11l111ll_opy_, bstack111l1ll1_opy_=True)
            bstack11111ll1_opy_ = results[bstack11l111_opy_ (u"ࠨࡰࡲࡨࡪ࡯ࡤࡴࠩচ")]
            os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡑࡕࡇࡍࡋࡓࡕࡔࡄࡘࡊࡊ࡟ࡔࡇࡏࡉࡈ࡚ࡏࡓࡕࠪছ")] = json.dumps(bstack11111ll1_opy_)
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦ࡮ࡰࡦࡨࠤࡸ࡫࡬ࡦࡥࡷࡳࡷࡹ࠺ࠡࡽࢀࠦজ").format(str(e)))
            return 0
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1lll1llll_opy_():
        import importlib
        if getattr(importlib, bstack11l111_opy_ (u"ࠫ࡫࡯࡮ࡥࡡ࡯ࡳࡦࡪࡥࡳࠩঝ"), False):
            bstack111l1l11_opy_ = importlib.find_loader(bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧঞ"))
        else:
            bstack111l1l11_opy_ = importlib.util.find_spec(bstack11l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨট"))
    def bstack111111ll_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1111111l_opy_ = -1
        if self.bstack11l1l11l_opy_ and bstack11l111_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧঠ") in self.bstack1lllll11l_opy_:
            self.bstack1111111l_opy_ = int(self.bstack1lllll11l_opy_[bstack11l111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨড")])
        try:
            bstack11l1l111_opy_ = [bstack11l111_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫঢ"), bstack11l111_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭ণ"), bstack11l111_opy_ (u"ࠫ࠲ࡶࠧত")]
            if self.bstack1111111l_opy_ >= 0:
                bstack11l1l111_opy_.extend([bstack11l111_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭থ"), bstack11l111_opy_ (u"࠭࠭࡯ࠩদ")])
            for arg in bstack11l1l111_opy_:
                self.bstack111111ll_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1llllll11_opy_(self):
        bstack11l11l11_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11l11l11_opy_ = bstack11l11l11_opy_
        return self.bstack11l11l11_opy_
    def bstack111ll1l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1lll1llll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11l11ll1_opy_)
    def bstack11111111_opy_(self, bstack11l11111_opy_):
        bstack111ll111_opy_ = Config.bstack111ll1ll_opy_()
        if bstack11l11111_opy_:
            self.bstack11l11l11_opy_.append(bstack11l111_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫধ"))
            self.bstack11l11l11_opy_.append(bstack11l111_opy_ (u"ࠨࡖࡵࡹࡪ࠭ন"))
        if bstack111ll111_opy_.bstack1lll1ll11_opy_():
            self.bstack11l11l11_opy_.append(bstack11l111_opy_ (u"ࠩ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ঩"))
            self.bstack11l11l11_opy_.append(bstack11l111_opy_ (u"ࠪࡘࡷࡻࡥࠨপ"))
        self.bstack11l11l11_opy_.append(bstack11l111_opy_ (u"ࠫ࠲ࡶࠧফ"))
        self.bstack11l11l11_opy_.append(bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠪব"))
        self.bstack11l11l11_opy_.append(bstack11l111_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨভ"))
        self.bstack11l11l11_opy_.append(bstack11l111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧম"))
        if self.bstack1111111l_opy_ > 1:
            self.bstack11l11l11_opy_.append(bstack11l111_opy_ (u"ࠨ࠯ࡱࠫয"))
            self.bstack11l11l11_opy_.append(str(self.bstack1111111l_opy_))
    def bstack1111llll_opy_(self):
        if bstack1llllllll_opy_.bstack111l111l_opy_(self.bstack1lllll11l_opy_):
             self.bstack11l11l11_opy_ += [
                bstack1llll111l_opy_.get(bstack11l111_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࠨর")), str(bstack1llllllll_opy_.bstack111lll1l_opy_(self.bstack1lllll11l_opy_)),
                bstack1llll111l_opy_.get(bstack11l111_opy_ (u"ࠪࡨࡪࡲࡡࡺࠩ঱")), str(bstack1llll111l_opy_.get(bstack11l111_opy_ (u"ࠫࡷ࡫ࡲࡶࡰ࠰ࡨࡪࡲࡡࡺࠩল")))
            ]
    def bstack111ll11l_opy_(self):
        bstack1lllll1l1_opy_ = []
        for spec in self.bstack11l111ll_opy_:
            bstack1111ll11_opy_ = [spec]
            bstack1111ll11_opy_ += self.bstack11l11l11_opy_
            bstack1lllll1l1_opy_.append(bstack1111ll11_opy_)
        self.bstack1lllll1l1_opy_ = bstack1lllll1l1_opy_
        return bstack1lllll1l1_opy_
    def bstack1111l11l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1llll11ll_opy_ = True
            return True
        except Exception as e:
            self.bstack1llll11ll_opy_ = False
        return self.bstack1llll11ll_opy_
    def bstack1111l111_opy_(self):
        bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡇࡦࡶࠣࡸ࡭࡫ࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡸ࡭࡫࡭ࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࠰࠱ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡵ࡮࡭ࡻࠣࡪࡱࡧࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࡴ࠻ࠢࡗ࡬ࡪࠦࡴࡰࡶࡤࡰࠥࡴࡵ࡮ࡤࡨࡶࠥࡵࡦࠡࡶࡨࡷࡹࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ঳")
        try:
            from bstack111lll11_opy_.plugin import bstack1llll11l1_opy_
            bstack1lll1lll1_opy_ = bstack1llll11l1_opy_(bstack111l11ll_opy_=self.bstack11l11l11_opy_, bstack111l1ll1_opy_=True)
            self.logger.info(bstack11l111_opy_ (u"ࠨࡃࡰ࡮࡯ࡩࡨࡺࡥࡥࠢࡾࢁࠥࡺࡥࡴࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠥ࡬ࡩ࡭ࡧࡶࠦ঴").format(bstack1lll1lll1_opy_[bstack11l111_opy_ (u"ࠧࡤࡱࡸࡲࡹ࠭঵")], len(bstack1lll1lll1_opy_[bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬশ")])))
            return bstack1lll1lll1_opy_[bstack11l111_opy_ (u"ࠩࡦࡳࡺࡴࡴࠨষ")]
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢস").format(e))
            return 0
    def bstack11111l1l_opy_(self, bstack111111l1_opy_, bstack111l1111_opy_):
        bstack111l1111_opy_[bstack11l111_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫহ")] = self.bstack1lllll11l_opy_
        multiprocessing.set_start_method(bstack11l111_opy_ (u"ࠬࡹࡰࡢࡹࡱࠫ঺"))
        bstack1111l1ll_opy_ = []
        manager = multiprocessing.Manager()
        bstack11l1111l_opy_ = manager.list()
        if bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ঻") in self.bstack1lllll11l_opy_:
            for index, platform in enumerate(self.bstack1lllll11l_opy_[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ়ࠪ")]):
                bstack1111l1ll_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack111111l1_opy_,
                                                            args=(self.bstack11l11l11_opy_, bstack111l1111_opy_, bstack11l1111l_opy_)))
            bstack11l11l1l_opy_ = len(self.bstack1lllll11l_opy_[bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫঽ")])
        else:
            bstack1111l1ll_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack111111l1_opy_,
                                                        args=(self.bstack11l11l11_opy_, bstack111l1111_opy_, bstack11l1111l_opy_)))
            bstack11l11l1l_opy_ = 1
        i = 0
        for t in bstack1111l1ll_opy_:
            os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩা")] = str(i)
            if bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ি") in self.bstack1lllll11l_opy_:
                os.environ[bstack11l111_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬী")] = json.dumps(self.bstack1lllll11l_opy_[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨু")][i % bstack11l11l1l_opy_])
            i += 1
            t.start()
        for t in bstack1111l1ll_opy_:
            t.join()
        return list(bstack11l1111l_opy_)
    @staticmethod
    def bstack1lllllll1_opy_(driver, bstack111l1l1l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11l111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪূ"), None)
        if item and getattr(item, bstack11l111_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࠩৃ"), None) and not getattr(item, bstack11l111_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࡤࡪ࡯࡯ࡧࠪৄ"), False):
            logger.info(
                bstack11l111_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠠࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡵࡻࡦࡿ࠮ࠣ৅"))
            bstack1llll1ll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack11l111l1_opy_.bstack11l11lll_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1llll1l11_opy_(self):
        bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡸࡴࠦࡢࡦࠢࡨࡼࡪࡩࡵࡵࡧࡧࠤࡧࡿࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡵࡵࡵࡲࡸࡸࠥࡵࡦࠡࡲࡼࡸࡪࡹࡴࠡ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ৆")
        try:
            from bstack111lll11_opy_.plugin import bstack1llll11l1_opy_
            bstack1lll1l1ll_opy_ = bstack1llll11l1_opy_(bstack111l11ll_opy_=self.bstack11l11l11_opy_, bstack111l1ll1_opy_=True)
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸࡪࡪࠠࡼࡿࠣࡸࡪࡹࡴࡴࠢ࡬ࡲࠥࢁࡽࠡࡨ࡬ࡰࡪࡹࠢে").format(bstack1lll1l1ll_opy_[bstack11l111_opy_ (u"ࠬࡩ࡯ࡶࡰࡷࠫৈ")], len(bstack1lll1l1ll_opy_[bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࠪ৉")])))
            return bstack1lll1l1ll_opy_[bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࠫ৊")]
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠾ࠥࢁࡽࠣো").format(e))
            return []