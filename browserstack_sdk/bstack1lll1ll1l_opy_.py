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
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1111l11l_opy_
from browserstack_sdk.bstack1111l111_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1lll11l11_opy_
from bstack_utils.bstack1111ll1l_opy_ import bstack1lll1l1ll_opy_
from bstack_utils.constants import bstack111ll111_opy_
from bstack_utils.bstack1lll1ll11_opy_ import bstack11111lll_opy_
class bstack111lll11_opy_:
    def __init__(self, args, logger, bstack1llll1l1l_opy_, bstack1lll1llll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1llll1l1l_opy_ = bstack1llll1l1l_opy_
        self.bstack1lll1llll_opy_ = bstack1lll1llll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1llll1l11_opy_ = []
        self.bstack111ll11l_opy_ = []
        self.bstack1llll11ll_opy_ = []
        self.bstack1111l1ll_opy_ = self.bstack1llll111l_opy_()
        self.bstack1lll1l111_opy_ = -1
    def bstack111111l1_opy_(self, bstack1111ll11_opy_):
        self.parse_args()
        self.bstack1111l1l1_opy_()
        self.bstack111l1ll1_opy_(bstack1111ll11_opy_)
        self.bstack111l11ll_opy_()
    def bstack1111llll_opy_(self):
        bstack1lll1ll11_opy_ = bstack11111lll_opy_.bstack111l11l1_opy_(self.bstack1llll1l1l_opy_, self.logger)
        if bstack1lll1ll11_opy_ is None:
            self.logger.warn(bstack11l111_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡲࡩࡲࡥࡳࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦশ"))
            return
        bstack1llllll1l_opy_ = False
        bstack1lll1ll11_opy_.bstack11111l1l_opy_(bstack11l111_opy_ (u"ࠤࡨࡲࡦࡨ࡬ࡦࡦࠥষ"), bstack1lll1ll11_opy_.bstack1llllll11_opy_())
        start_time = time.time()
        if bstack1lll1ll11_opy_.bstack1llllll11_opy_():
            test_files = self.bstack1llllllll_opy_()
            bstack1llllll1l_opy_ = True
            bstack111l1l11_opy_ = bstack1lll1ll11_opy_.bstack1lll1l11l_opy_(test_files)
            if bstack111l1l11_opy_:
                self.bstack1llll1l11_opy_ = [os.path.normpath(item).replace(bstack11l111_opy_ (u"ࠪࡠࡡ࠭স"), bstack11l111_opy_ (u"ࠫ࠴࠭হ")) for item in bstack111l1l11_opy_]
                self.__1lll11lll_opy_()
                bstack1lll1ll11_opy_.bstack111ll1ll_opy_(bstack1llllll1l_opy_)
                self.logger.info(bstack11l111_opy_ (u"࡚ࠧࡥࡴࡶࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡶࡵ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥ঺").format(self.bstack1llll1l11_opy_))
            else:
                self.logger.info(bstack11l111_opy_ (u"ࠨࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡦࡴࡨࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡣࡻࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦ঻"))
        bstack1lll1ll11_opy_.bstack11111l1l_opy_(bstack11l111_opy_ (u"ࠢࡵ࡫ࡰࡩ࡙ࡧ࡫ࡦࡰࡗࡳࡆࡶࡰ࡭ࡻ়ࠥ"), int((time.time() - start_time) * 1000)) # bstack111l1111_opy_ to bstack111l1lll_opy_
    def __1lll11lll_opy_(self):
        bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡳࡦ࡮ࡩ࠲ࡸࡶࡥࡤࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡦࡳࡱࡲࡥࡤࡶࠣࡥࡱࡲࠠ࡯ࡱࡧࡩ࡮ࡪࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨঽ")
        bstack111ll1l1_opy_ = []
        try:
            from browserstack_sdk.bstack11ll1l11_opy_ import bstack11l1llll_opy_
            results = bstack11l1llll_opy_(bstack11ll11l1_opy_=self.bstack1llll1l11_opy_, bstack11l1l1ll_opy_=True)
            if not results.get(bstack11l111_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪা"), False):
                self.logger.error(bstack11l111_opy_ (u"ࠥࡘࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤি").format(results.get(bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪী"), bstack11l111_opy_ (u"࡛ࠬ࡮࡬ࡰࡲࡻࡳࠦࡥࡳࡴࡲࡶࠬু"))))
                return 0
            bstack111ll1l1_opy_ = results.get(bstack11l111_opy_ (u"࠭࡮ࡰࡦࡨ࡭ࡩࡹࠧূ"), [])
            if bstack111ll1l1_opy_:
                os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡏࡓࡅࡋࡉࡘ࡚ࡒࡂࡖࡈࡈࡤ࡙ࡅࡍࡇࡆࡘࡔࡘࡓࠨৃ")] = json.dumps(bstack111ll1l1_opy_)
                self.logger.info(bstack11l111_opy_ (u"ࠣࡅࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࢀࢃࠠࡵࡧࡶࡸࠥࡴ࡯ࡥࡧ࡬ࡨࡸࠦࡦࡰࡴࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠥৄ").format(len(bstack111ll1l1_opy_)))
            else:
                self.logger.warn(bstack11l111_opy_ (u"ࠤࡑࡳࠥࡺࡥࡴࡶࡶࠤࡨࡵ࡬࡭ࡧࡦࡸࡪࡪࠠࡧࡴࡲࡱࠥࡹࡰࡦࡥࠣࡪ࡮ࡲࡥࡴ࠼ࠣࡿࢂࠨ৅").format(self.bstack1llll1l11_opy_))
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦ࡮ࡰࡦࡨࠤࡸ࡫࡬ࡦࡥࡷࡳࡷࡹ࠺ࠡࡽࢀࠦ৆").format(str(e)))
            import traceback
            self.logger.error(bstack11l111_opy_ (u"࡙ࠦࡸࡡࡤࡧࡥࡥࡨࡱ࠺ࠡࡽࢀࠦে").format(traceback.format_exc()))
            return 0
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1lll111ll_opy_():
        import importlib
        if getattr(importlib, bstack11l111_opy_ (u"ࠬ࡬ࡩ࡯ࡦࡢࡰࡴࡧࡤࡦࡴࠪৈ"), False):
            bstack111l111l_opy_ = importlib.find_loader(bstack11l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨ৉"))
        else:
            bstack111l111l_opy_ = importlib.util.find_spec(bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩ৊"))
    def bstack1lllll111_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1lll1l111_opy_ = -1
        if self.bstack1lll1llll_opy_ and bstack11l111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨো") in self.bstack1llll1l1l_opy_:
            self.bstack1lll1l111_opy_ = int(self.bstack1llll1l1l_opy_[bstack11l111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩৌ")])
        try:
            bstack1111111l_opy_ = [bstack11l111_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶ্ࠬ"), bstack11l111_opy_ (u"ࠫ࠲࠳ࡰ࡭ࡷࡪ࡭ࡳࡹࠧৎ"), bstack11l111_opy_ (u"ࠬ࠳ࡰࠨ৏")]
            if self.bstack1lll1l111_opy_ >= 0:
                bstack1111111l_opy_.extend([bstack11l111_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ৐"), bstack11l111_opy_ (u"ࠧ࠮ࡰࠪ৑")])
            for arg in bstack1111111l_opy_:
                self.bstack1lllll111_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1111l1l1_opy_(self):
        bstack111ll11l_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack111ll11l_opy_ = bstack111ll11l_opy_
        return self.bstack111ll11l_opy_
    def bstack1lll1l1l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1lll111ll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1lll11l11_opy_)
    def bstack111l1ll1_opy_(self, bstack1111ll11_opy_):
        bstack11111l11_opy_ = Config.bstack111l11l1_opy_()
        if bstack1111ll11_opy_:
            self.bstack111ll11l_opy_.append(bstack11l111_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ৒"))
            self.bstack111ll11l_opy_.append(bstack11l111_opy_ (u"ࠩࡗࡶࡺ࡫ࠧ৓"))
        if bstack11111l11_opy_.bstack111l1l1l_opy_():
            self.bstack111ll11l_opy_.append(bstack11l111_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ৔"))
            self.bstack111ll11l_opy_.append(bstack11l111_opy_ (u"࡙ࠫࡸࡵࡦࠩ৕"))
        self.bstack111ll11l_opy_.append(bstack11l111_opy_ (u"ࠬ࠳ࡰࠨ৖"))
        self.bstack111ll11l_opy_.append(bstack11l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠫৗ"))
        self.bstack111ll11l_opy_.append(bstack11l111_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩ৘"))
        self.bstack111ll11l_opy_.append(bstack11l111_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ৙"))
        if self.bstack1lll1l111_opy_ > 1:
            self.bstack111ll11l_opy_.append(bstack11l111_opy_ (u"ࠩ࠰ࡲࠬ৚"))
            self.bstack111ll11l_opy_.append(str(self.bstack1lll1l111_opy_))
    def bstack111l11ll_opy_(self):
        if bstack1lll1l1ll_opy_.bstack1lll111l1_opy_(self.bstack1llll1l1l_opy_):
             self.bstack111ll11l_opy_ += [
                bstack111ll111_opy_.get(bstack11l111_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࠩ৛")), str(bstack1lll1l1ll_opy_.bstack1lllll1l1_opy_(self.bstack1llll1l1l_opy_)),
                bstack111ll111_opy_.get(bstack11l111_opy_ (u"ࠫࡩ࡫࡬ࡢࡻࠪড়")), str(bstack111ll111_opy_.get(bstack11l111_opy_ (u"ࠬࡸࡥࡳࡷࡱ࠱ࡩ࡫࡬ࡢࡻࠪঢ়")))
            ]
    def bstack1llll11l1_opy_(self):
        bstack1llll11ll_opy_ = []
        for spec in self.bstack1llll1l11_opy_:
            bstack1111lll1_opy_ = [spec]
            bstack1111lll1_opy_ += self.bstack111ll11l_opy_
            bstack1llll11ll_opy_.append(bstack1111lll1_opy_)
        self.bstack1llll11ll_opy_ = bstack1llll11ll_opy_
        return bstack1llll11ll_opy_
    def bstack1llll111l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1111l1ll_opy_ = True
            return True
        except Exception as e:
            self.bstack1111l1ll_opy_ = False
        return self.bstack1111l1ll_opy_
    def bstack1lllll11l_opy_(self):
        bstack11l111_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡋࡪࡺࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥࡽࡩࡵࡪࡲࡹࡹࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡵࡪࡨࡱࠥࡻࡳࡪࡰࡪࠤࡵࡿࡴࡦࡵࡷࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡭ࡳࡺ࠺ࠡࡖ࡫ࡩࠥࡺ࡯ࡵࡣ࡯ࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࡣࡰ࡮࡯ࡩࡨࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ৞")
        try:
            from browserstack_sdk.bstack11ll1l11_opy_ import bstack11l1llll_opy_
            bstack1lllll1ll_opy_ = bstack11l1llll_opy_(bstack11l1ll11_opy_=self.bstack111ll11l_opy_, bstack11l1l1ll_opy_=True)
            if not bstack1lllll1ll_opy_.get(bstack11l111_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨয়"), False):
                self.logger.error(bstack11l111_opy_ (u"ࠣࡖࡨࡷࡹࠦࡣࡰࡷࡱࡸࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡿࢂࠨৠ").format(bstack1lllll1ll_opy_.get(bstack11l111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨৡ"), bstack11l111_opy_ (u"࡙ࠪࡳࡱ࡮ࡰࡹࡱࠤࡪࡸࡲࡰࡴࠪৢ"))))
                return 0
            count = bstack1lllll1ll_opy_.get(bstack11l111_opy_ (u"ࠫࡨࡵࡵ࡯ࡶࠪৣ"), 0)
            test_files = bstack1lllll1ll_opy_.get(bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴࠩ৤"), [])
            self.logger.info(bstack11l111_opy_ (u"ࠨࡃࡰ࡮࡯ࡩࡨࡺࡥࡥࠢࡾࢁࠥࡺࡥࡴࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠥ࡬ࡩ࡭ࡧࡶࠦ৥").format(count, len(test_files)))
            return count
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥࡲࡹࡳࡺ࠺ࠡࡽࢀࠦ০").format(e))
            import traceback
            self.logger.error(bstack11l111_opy_ (u"ࠣࡖࡵࡥࡨ࡫ࡢࡢࡥ࡮࠾ࠥࢁࡽࠣ১").format(traceback.format_exc()))
            return 0
    def bstack1llll1ll1_opy_(self, bstack1lll11ll1_opy_, bstack111111l1_opy_):
        bstack111111l1_opy_[bstack11l111_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ২")] = self.bstack1llll1l1l_opy_
        multiprocessing.set_start_method(bstack11l111_opy_ (u"ࠪࡷࡵࡧࡷ࡯ࠩ৩"))
        bstack1llll1111_opy_ = []
        manager = multiprocessing.Manager()
        bstack1lll11l1l_opy_ = manager.list()
        if bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ৪") in self.bstack1llll1l1l_opy_:
            for index, platform in enumerate(self.bstack1llll1l1l_opy_[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৫")]):
                bstack1llll1111_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1lll11ll1_opy_,
                                                            args=(self.bstack111ll11l_opy_, bstack111111l1_opy_, bstack1lll11l1l_opy_)))
            bstack11111ll1_opy_ = len(self.bstack1llll1l1l_opy_[bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৬")])
        else:
            bstack1llll1111_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1lll11ll1_opy_,
                                                        args=(self.bstack111ll11l_opy_, bstack111111l1_opy_, bstack1lll11l1l_opy_)))
            bstack11111ll1_opy_ = 1
        i = 0
        for t in bstack1llll1111_opy_:
            os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ৭")] = str(i)
            if bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ৮") in self.bstack1llll1l1l_opy_:
                os.environ[bstack11l111_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ৯")] = json.dumps(self.bstack1llll1l1l_opy_[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ৰ")][i % bstack11111ll1_opy_])
            i += 1
            t.start()
        for t in bstack1llll1111_opy_:
            t.join()
        return list(bstack1lll11l1l_opy_)
    @staticmethod
    def bstack11111111_opy_(driver, bstack111111ll_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨৱ"), None)
        if item and getattr(item, bstack11l111_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫ࠧ৲"), None) and not getattr(item, bstack11l111_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡰࡲࡢࡨࡴࡴࡥࠨ৳"), False):
            logger.info(
                bstack11l111_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠨ৴"))
            bstack1lll1lll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1111l11l_opy_.bstack1lllllll1_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1llllllll_opy_(self):
        bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࠦࡴࡩࡧࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡶࡲࠤࡧ࡫ࠠࡦࡺࡨࡧࡺࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ৵")
        try:
            from browserstack_sdk.bstack11ll1l11_opy_ import bstack11l1llll_opy_
            bstack1llll1lll_opy_ = bstack11l1llll_opy_(bstack11l1ll11_opy_=self.bstack111ll11l_opy_, bstack11l1l1ll_opy_=True)
            if not bstack1llll1lll_opy_.get(bstack11l111_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ৶"), False):
                self.logger.error(bstack11l111_opy_ (u"ࠥࡘࡪࡹࡴࠡࡨ࡬ࡰࡪࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࢀࢃࠢ৷").format(bstack1llll1lll_opy_.get(bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ৸"), bstack11l111_opy_ (u"࡛ࠬ࡮࡬ࡰࡲࡻࡳࠦࡥࡳࡴࡲࡶࠬ৹"))))
                return []
            test_files = bstack1llll1lll_opy_.get(bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࠪ৺"), [])
            count = bstack1llll1lll_opy_.get(bstack11l111_opy_ (u"ࠧࡤࡱࡸࡲࡹ࠭৻"), 0)
            self.logger.debug(bstack11l111_opy_ (u"ࠣࡅࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࢀࢃࠠࡵࡧࡶࡸࡸࠦࡩ࡯ࠢࡾࢁࠥ࡬ࡩ࡭ࡧࡶࠦৼ").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤ৽").format(e))
            import traceback
            self.logger.error(bstack11l111_opy_ (u"ࠥࡘࡷࡧࡣࡦࡤࡤࡧࡰࡀࠠࡼࡿࠥ৾").format(traceback.format_exc()))
            return []