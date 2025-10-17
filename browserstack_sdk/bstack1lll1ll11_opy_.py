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
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1lll1ll1l_opy_
from browserstack_sdk.bstack111l1lll_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l11l1l_opy_
from bstack_utils.bstack111ll11l_opy_ import bstack1lllll1ll_opy_
from bstack_utils.constants import bstack1lllll111_opy_
from bstack_utils.bstack1111ll1l_opy_ import bstack1111l11l_opy_
class bstack11l111ll_opy_:
    def __init__(self, args, logger, bstack1lllll11l_opy_, bstack111ll1ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lllll11l_opy_ = bstack1lllll11l_opy_
        self.bstack111ll1ll_opy_ = bstack111ll1ll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1llll1lll_opy_ = []
        self.bstack1lllll1l1_opy_ = []
        self.bstack111l1ll1_opy_ = []
        self.bstack1llll11ll_opy_ = self.bstack1llllll1l_opy_()
        self.bstack1111ll11_opy_ = -1
    def bstack111l1111_opy_(self, bstack11l11l11_opy_):
        self.parse_args()
        self.bstack1lllllll1_opy_()
        self.bstack1llllll11_opy_(bstack11l11l11_opy_)
        self.bstack1111l111_opy_()
    def bstack1111llll_opy_(self):
        bstack1111ll1l_opy_ = bstack1111l11l_opy_.bstack111111ll_opy_(self.bstack1lllll11l_opy_, self.logger)
        if bstack1111ll1l_opy_ is None:
            self.logger.warn(bstack11111_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡩࡣࡱࡨࡱ࡫ࡲࠡ࡫ࡶࠤࡳࡵࡴࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡩ࠴ࠠࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥ঒"))
            return
        bstack11111ll1_opy_ = False
        bstack1111ll1l_opy_.bstack111l1l1l_opy_(bstack11111_opy_ (u"ࠣࡧࡱࡥࡧࡲࡥࡥࠤও"), bstack1111ll1l_opy_.bstack1llll1111_opy_())
        start_time = time.time()
        if bstack1111ll1l_opy_.bstack1llll1111_opy_():
            test_files = self.bstack11l11111_opy_()
            bstack11111ll1_opy_ = True
            bstack1lll1l1ll_opy_ = bstack1111ll1l_opy_.bstack111l11ll_opy_(test_files)
            if bstack1lll1l1ll_opy_:
                self.bstack1llll1lll_opy_ = [os.path.normpath(item).replace(bstack11111_opy_ (u"ࠩ࡟ࡠࠬঔ"), bstack11111_opy_ (u"ࠪ࠳ࠬক")) for item in bstack1lll1l1ll_opy_]
                self.__1llll1ll1_opy_()
                bstack1111ll1l_opy_.bstack111111l1_opy_(bstack11111ll1_opy_)
                self.logger.info(bstack11111_opy_ (u"࡙ࠦ࡫ࡳࡵࡵࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡵࡴ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤখ").format(self.bstack1llll1lll_opy_))
            else:
                self.logger.info(bstack11111_opy_ (u"ࠧࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡥࡳࡧࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡢࡺࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥগ"))
        bstack1111ll1l_opy_.bstack111l1l1l_opy_(bstack11111_opy_ (u"ࠨࡴࡪ࡯ࡨࡘࡦࡱࡥ࡯ࡖࡲࡅࡵࡶ࡬ࡺࠤঘ"), int((time.time() - start_time) * 1000)) # bstack1llll11l1_opy_ to bstack111ll1l1_opy_
    def __1llll1ll1_opy_(self):
        bstack11111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡹࡥ࡭ࡨ࠱ࡷࡵ࡫ࡣࡠࡨ࡬ࡰࡪࡹࠬࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡤࡰࡱࠦ࡮ࡰࡦࡨ࡭ࡩࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦঙ")
        bstack111l111l_opy_ = []
        try:
            from pytest_browserstackplugin.plugin import bstack1llllllll_opy_
            results = bstack1llllllll_opy_(bstack11l1l111_opy_=self.bstack1llll1lll_opy_, bstack1llll111l_opy_=True)
            bstack111l111l_opy_ = results[bstack11111_opy_ (u"ࠨࡰࡲࡨࡪ࡯ࡤࡴࠩচ")]
            os.environ[bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡑࡕࡇࡍࡋࡓࡕࡔࡄࡘࡊࡊ࡟ࡔࡇࡏࡉࡈ࡚ࡏࡓࡕࠪছ")] = json.dumps(bstack111l111l_opy_)
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦ࡮ࡰࡦࡨࠤࡸ࡫࡬ࡦࡥࡷࡳࡷࡹ࠺ࠡࡽࢀࠦজ").format(str(e)))
            return 0
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111lll11_opy_():
        import importlib
        if getattr(importlib, bstack11111_opy_ (u"ࠫ࡫࡯࡮ࡥࡡ࡯ࡳࡦࡪࡥࡳࠩঝ"), False):
            bstack11111lll_opy_ = importlib.find_loader(bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧঞ"))
        else:
            bstack11111lll_opy_ = importlib.util.find_spec(bstack11111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨট"))
    def bstack11l111l1_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1111ll11_opy_ = -1
        if self.bstack111ll1ll_opy_ and bstack11111_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧঠ") in self.bstack1lllll11l_opy_:
            self.bstack1111ll11_opy_ = int(self.bstack1lllll11l_opy_[bstack11111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨড")])
        try:
            bstack11111l1l_opy_ = [bstack11111_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫঢ"), bstack11111_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭ণ"), bstack11111_opy_ (u"ࠫ࠲ࡶࠧত")]
            if self.bstack1111ll11_opy_ >= 0:
                bstack11111l1l_opy_.extend([bstack11111_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭থ"), bstack11111_opy_ (u"࠭࠭࡯ࠩদ")])
            for arg in bstack11111l1l_opy_:
                self.bstack11l111l1_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1lllllll1_opy_(self):
        bstack1lllll1l1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1lllll1l1_opy_ = bstack1lllll1l1_opy_
        return self.bstack1lllll1l1_opy_
    def bstack1111lll1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111lll11_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11l11l1l_opy_)
    def bstack1llllll11_opy_(self, bstack11l11l11_opy_):
        bstack11l1111l_opy_ = Config.bstack111111ll_opy_()
        if bstack11l11l11_opy_:
            self.bstack1lllll1l1_opy_.append(bstack11111_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫধ"))
            self.bstack1lllll1l1_opy_.append(bstack11111_opy_ (u"ࠨࡖࡵࡹࡪ࠭ন"))
        if bstack11l1111l_opy_.bstack1lll1lll1_opy_():
            self.bstack1lllll1l1_opy_.append(bstack11111_opy_ (u"ࠩ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ঩"))
            self.bstack1lllll1l1_opy_.append(bstack11111_opy_ (u"ࠪࡘࡷࡻࡥࠨপ"))
        self.bstack1lllll1l1_opy_.append(bstack11111_opy_ (u"ࠫ࠲ࡶࠧফ"))
        self.bstack1lllll1l1_opy_.append(bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠪব"))
        self.bstack1lllll1l1_opy_.append(bstack11111_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨভ"))
        self.bstack1lllll1l1_opy_.append(bstack11111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧম"))
        if self.bstack1111ll11_opy_ > 1:
            self.bstack1lllll1l1_opy_.append(bstack11111_opy_ (u"ࠨ࠯ࡱࠫয"))
            self.bstack1lllll1l1_opy_.append(str(self.bstack1111ll11_opy_))
    def bstack1111l111_opy_(self):
        if bstack1lllll1ll_opy_.bstack1111l1ll_opy_(self.bstack1lllll11l_opy_):
             self.bstack1lllll1l1_opy_ += [
                bstack1lllll111_opy_.get(bstack11111_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࠨর")), str(bstack1lllll1ll_opy_.bstack1111l1l1_opy_(self.bstack1lllll11l_opy_)),
                bstack1lllll111_opy_.get(bstack11111_opy_ (u"ࠪࡨࡪࡲࡡࡺࠩ঱")), str(bstack1lllll111_opy_.get(bstack11111_opy_ (u"ࠫࡷ࡫ࡲࡶࡰ࠰ࡨࡪࡲࡡࡺࠩল")))
            ]
    def bstack111l1l11_opy_(self):
        bstack111l1ll1_opy_ = []
        for spec in self.bstack1llll1lll_opy_:
            bstack11l11lll_opy_ = [spec]
            bstack11l11lll_opy_ += self.bstack1lllll1l1_opy_
            bstack111l1ll1_opy_.append(bstack11l11lll_opy_)
        self.bstack111l1ll1_opy_ = bstack111l1ll1_opy_
        return bstack111l1ll1_opy_
    def bstack1llllll1l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1llll11ll_opy_ = True
            return True
        except Exception as e:
            self.bstack1llll11ll_opy_ = False
        return self.bstack1llll11ll_opy_
    def bstack11111l11_opy_(self):
        bstack11111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡇࡦࡶࠣࡸ࡭࡫ࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡸ࡭࡫࡭ࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢ࠰࠱ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡵ࡮࡭ࡻࠣࡪࡱࡧࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࡴ࠻ࠢࡗ࡬ࡪࠦࡴࡰࡶࡤࡰࠥࡴࡵ࡮ࡤࡨࡶࠥࡵࡦࠡࡶࡨࡷࡹࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ঳")
        try:
            from pytest_browserstackplugin.plugin import bstack1llllllll_opy_
            bstack111llll1_opy_ = bstack1llllllll_opy_(bstack111l11l1_opy_=self.bstack1lllll1l1_opy_, bstack1llll111l_opy_=True)
            self.logger.info(bstack11111_opy_ (u"ࠨࡃࡰ࡮࡯ࡩࡨࡺࡥࡥࠢࡾࢁࠥࡺࡥࡴࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠥ࡬ࡩ࡭ࡧࡶࠦ঴").format(bstack111llll1_opy_[bstack11111_opy_ (u"ࠧࡤࡱࡸࡲࡹ࠭঵")], len(bstack111llll1_opy_[bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬশ")])))
            return bstack111llll1_opy_[bstack11111_opy_ (u"ࠩࡦࡳࡺࡴࡴࠨষ")]
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢস").format(e))
            return 0
    def bstack111lll1l_opy_(self, bstack1111111l_opy_, bstack111l1111_opy_):
        bstack111l1111_opy_[bstack11111_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫহ")] = self.bstack1lllll11l_opy_
        multiprocessing.set_start_method(bstack11111_opy_ (u"ࠬࡹࡰࡢࡹࡱࠫ঺"))
        bstack111lllll_opy_ = []
        manager = multiprocessing.Manager()
        bstack11l1l11l_opy_ = manager.list()
        if bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ঻") in self.bstack1lllll11l_opy_:
            for index, platform in enumerate(self.bstack1lllll11l_opy_[bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ়ࠪ")]):
                bstack111lllll_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1111111l_opy_,
                                                            args=(self.bstack1lllll1l1_opy_, bstack111l1111_opy_, bstack11l1l11l_opy_)))
            bstack111ll111_opy_ = len(self.bstack1lllll11l_opy_[bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫঽ")])
        else:
            bstack111lllll_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1111111l_opy_,
                                                        args=(self.bstack1lllll1l1_opy_, bstack111l1111_opy_, bstack11l1l11l_opy_)))
            bstack111ll111_opy_ = 1
        i = 0
        for t in bstack111lllll_opy_:
            os.environ[bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩা")] = str(i)
            if bstack11111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ি") in self.bstack1lllll11l_opy_:
                os.environ[bstack11111_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬী")] = json.dumps(self.bstack1lllll11l_opy_[bstack11111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨু")][i % bstack111ll111_opy_])
            i += 1
            t.start()
        for t in bstack111lllll_opy_:
            t.join()
        return list(bstack11l1l11l_opy_)
    @staticmethod
    def bstack1lll1llll_opy_(driver, bstack1llll1l11_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪূ"), None)
        if item and getattr(item, bstack11111_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࠩৃ"), None) and not getattr(item, bstack11111_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࡤࡪ࡯࡯ࡧࠪৄ"), False):
            logger.info(
                bstack11111_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠠࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡵࡻࡦࡿ࠮ࠣ৅"))
            bstack11l11ll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1lll1ll1l_opy_.bstack1llll1l1l_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack11l11111_opy_(self):
        bstack11111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡸࡴࠦࡢࡦࠢࡨࡼࡪࡩࡵࡵࡧࡧࠤࡧࡿࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡵࡵࡵࡲࡸࡸࠥࡵࡦࠡࡲࡼࡸࡪࡹࡴࠡ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ৆")
        try:
            from pytest_browserstackplugin.plugin import bstack1llllllll_opy_
            bstack11111111_opy_ = bstack1llllllll_opy_(bstack111l11l1_opy_=self.bstack1lllll1l1_opy_, bstack1llll111l_opy_=True)
            self.logger.debug(bstack11111_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸࡪࡪࠠࡼࡿࠣࡸࡪࡹࡴࡴࠢ࡬ࡲࠥࢁࡽࠡࡨ࡬ࡰࡪࡹࠢে").format(bstack11111111_opy_[bstack11111_opy_ (u"ࠬࡩ࡯ࡶࡰࡷࠫৈ")], len(bstack11111111_opy_[bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࠪ৉")])))
            return bstack11111111_opy_[bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࠫ৊")]
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠾ࠥࢁࡽࠣো").format(e))
            return []