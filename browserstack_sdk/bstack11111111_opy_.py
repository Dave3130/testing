# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1111ll1l_opy_
from browserstack_sdk.bstack1llll11l1_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1111l111_opy_
from bstack_utils.bstack111l1l1l_opy_ import bstack111l11ll_opy_
from bstack_utils.constants import bstack1111l11l_opy_
from bstack_utils.bstack1llll1ll1_opy_ import bstack1lllll1ll_opy_
class bstack111ll11l_opy_:
    def __init__(self, args, logger, bstack1lll111l1_opy_, bstack111lll11_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll111l1_opy_ = bstack1lll111l1_opy_
        self.bstack111lll11_opy_ = bstack111lll11_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1lll11ll1_opy_ = []
        self.bstack1lll1l1ll_opy_ = []
        self.bstack1lll1l11l_opy_ = []
        self.bstack111l1l11_opy_ = self.bstack1111111l_opy_()
        self.bstack1lll11lll_opy_ = -1
    def bstack11111l1l_opy_(self, bstack1lll1ll11_opy_):
        self.parse_args()
        self.bstack1lll11l1l_opy_()
        self.bstack111111ll_opy_(bstack1lll1ll11_opy_)
        self.bstack1llll1lll_opy_()
    def bstack1lll1l1l1_opy_(self):
        bstack1llll1ll1_opy_ = bstack1lllll1ll_opy_.bstack1111l1ll_opy_(self.bstack1lll111l1_opy_, self.logger)
        if bstack1llll1ll1_opy_ is None:
            self.logger.warn(bstack1lllll1l_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡲࡩࡲࡥࡳࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦশ"))
            return
        bstack1lllll1l1_opy_ = False
        bstack1llll1ll1_opy_.bstack1llllll11_opy_(bstack1lllll1l_opy_ (u"ࠤࡨࡲࡦࡨ࡬ࡦࡦࠥষ"), bstack1llll1ll1_opy_.bstack1llll11ll_opy_())
        start_time = time.time()
        if bstack1llll1ll1_opy_.bstack1llll11ll_opy_():
            test_files = self.bstack111l1111_opy_()
            bstack1lllll1l1_opy_ = True
            bstack1lllll111_opy_ = bstack1llll1ll1_opy_.bstack1lll11l11_opy_(test_files)
            if bstack1lllll111_opy_:
                self.bstack1lll11ll1_opy_ = [os.path.normpath(item).replace(bstack1lllll1l_opy_ (u"ࠪࡠࡡ࠭স"), bstack1lllll1l_opy_ (u"ࠫ࠴࠭হ")) for item in bstack1lllll111_opy_]
                self.__1lll111ll_opy_()
                bstack1llll1ll1_opy_.bstack1111l1l1_opy_(bstack1lllll1l1_opy_)
                self.logger.info(bstack1lllll1l_opy_ (u"࡚ࠧࡥࡴࡶࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡶࡵ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥ঺").format(self.bstack1lll11ll1_opy_))
            else:
                self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡦࡴࡨࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡣࡻࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦ঻"))
        bstack1llll1ll1_opy_.bstack1llllll11_opy_(bstack1lllll1l_opy_ (u"ࠢࡵ࡫ࡰࡩ࡙ࡧ࡫ࡦࡰࡗࡳࡆࡶࡰ࡭ࡻ়ࠥ"), int((time.time() - start_time) * 1000)) # bstack11111ll1_opy_ to bstack11111l11_opy_
    def __1lll111ll_opy_(self):
        bstack1lllll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡳࡦ࡮ࡩ࠲ࡸࡶࡥࡤࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡦࡳࡱࡲࡥࡤࡶࠣࡥࡱࡲࠠ࡯ࡱࡧࡩ࡮ࡪࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨঽ")
        bstack1llll1111_opy_ = []
        try:
            from browserstack_sdk.bstack11ll1lll_opy_ import bstack11l1llll_opy_
            results = bstack11l1llll_opy_(bstack11l1l1ll_opy_=self.bstack1lll11ll1_opy_, bstack11l1ll1l_opy_=True)
            if not results.get(bstack1lllll1l_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪা"), False):
                self.logger.error(bstack1lllll1l_opy_ (u"ࠥࡘࡪࡹࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤি").format(results.get(bstack1lllll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪী"), bstack1lllll1l_opy_ (u"࡛ࠬ࡮࡬ࡰࡲࡻࡳࠦࡥࡳࡴࡲࡶࠬু"))))
                return 0
            bstack1llll1111_opy_ = results.get(bstack1lllll1l_opy_ (u"࠭࡮ࡰࡦࡨ࡭ࡩࡹࠧূ"), [])
            if bstack1llll1111_opy_:
                os.environ[bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡏࡓࡅࡋࡉࡘ࡚ࡒࡂࡖࡈࡈࡤ࡙ࡅࡍࡇࡆࡘࡔࡘࡓࠨৃ")] = json.dumps(bstack1llll1111_opy_)
                self.logger.info(bstack1lllll1l_opy_ (u"ࠣࡅࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࢀࢃࠠࡵࡧࡶࡸࠥࡴ࡯ࡥࡧ࡬ࡨࡸࠦࡦࡰࡴࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠥৄ").format(len(bstack1llll1111_opy_)))
            else:
                self.logger.warn(bstack1lllll1l_opy_ (u"ࠤࡑࡳࠥࡺࡥࡴࡶࡶࠤࡨࡵ࡬࡭ࡧࡦࡸࡪࡪࠠࡧࡴࡲࡱࠥࡹࡰࡦࡥࠣࡪ࡮ࡲࡥࡴ࠼ࠣࡿࢂࠨ৅").format(self.bstack1lll11ll1_opy_))
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦ࡮ࡰࡦࡨࠤࡸ࡫࡬ࡦࡥࡷࡳࡷࡹ࠺ࠡࡽࢀࠦ৆").format(str(e)))
            import traceback
            self.logger.error(bstack1lllll1l_opy_ (u"࡙ࠦࡸࡡࡤࡧࡥࡥࡨࡱ࠺ࠡࡽࢀࠦে").format(traceback.format_exc()))
            return 0
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111ll1l1_opy_():
        import importlib
        if getattr(importlib, bstack1lllll1l_opy_ (u"ࠬ࡬ࡩ࡯ࡦࡢࡰࡴࡧࡤࡦࡴࠪৈ"), False):
            bstack1llll1l1l_opy_ = importlib.find_loader(bstack1lllll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨ৉"))
        else:
            bstack1llll1l1l_opy_ = importlib.util.find_spec(bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩ৊"))
    def bstack111ll1ll_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1lll11lll_opy_ = -1
        if self.bstack111lll11_opy_ and bstack1lllll1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨো") in self.bstack1lll111l1_opy_:
            self.bstack1lll11lll_opy_ = int(self.bstack1lll111l1_opy_[bstack1lllll1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩৌ")])
        try:
            bstack111l11l1_opy_ = [bstack1lllll1l_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶ্ࠬ"), bstack1lllll1l_opy_ (u"ࠫ࠲࠳ࡰ࡭ࡷࡪ࡭ࡳࡹࠧৎ"), bstack1lllll1l_opy_ (u"ࠬ࠳ࡰࠨ৏")]
            if self.bstack1lll11lll_opy_ >= 0:
                bstack111l11l1_opy_.extend([bstack1lllll1l_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ৐"), bstack1lllll1l_opy_ (u"ࠧ࠮ࡰࠪ৑")])
            for arg in bstack111l11l1_opy_:
                self.bstack111ll1ll_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1lll11l1l_opy_(self):
        bstack1lll1l1ll_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1lll1l1ll_opy_ = bstack1lll1l1ll_opy_
        return self.bstack1lll1l1ll_opy_
    def bstack111l1lll_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111ll1l1_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1111l111_opy_)
    def bstack111111ll_opy_(self, bstack1lll1ll11_opy_):
        bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
        if bstack1lll1ll11_opy_:
            self.bstack1lll1l1ll_opy_.append(bstack1lllll1l_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ৒"))
            self.bstack1lll1l1ll_opy_.append(bstack1lllll1l_opy_ (u"ࠩࡗࡶࡺ࡫ࠧ৓"))
        if bstack1lll1ll1l_opy_.bstack111ll111_opy_():
            self.bstack1lll1l1ll_opy_.append(bstack1lllll1l_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ৔"))
            self.bstack1lll1l1ll_opy_.append(bstack1lllll1l_opy_ (u"࡙ࠫࡸࡵࡦࠩ৕"))
        self.bstack1lll1l1ll_opy_.append(bstack1lllll1l_opy_ (u"ࠬ࠳ࡰࠨ৖"))
        self.bstack1lll1l1ll_opy_.append(bstack1lllll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠫৗ"))
        self.bstack1lll1l1ll_opy_.append(bstack1lllll1l_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩ৘"))
        self.bstack1lll1l1ll_opy_.append(bstack1lllll1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ৙"))
        if self.bstack1lll11lll_opy_ > 1:
            self.bstack1lll1l1ll_opy_.append(bstack1lllll1l_opy_ (u"ࠩ࠰ࡲࠬ৚"))
            self.bstack1lll1l1ll_opy_.append(str(self.bstack1lll11lll_opy_))
    def bstack1llll1lll_opy_(self):
        if bstack111l11ll_opy_.bstack1111lll1_opy_(self.bstack1lll111l1_opy_):
             self.bstack1lll1l1ll_opy_ += [
                bstack1111l11l_opy_.get(bstack1lllll1l_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࠩ৛")), str(bstack111l11ll_opy_.bstack1llllllll_opy_(self.bstack1lll111l1_opy_)),
                bstack1111l11l_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡩ࡫࡬ࡢࡻࠪড়")), str(bstack1111l11l_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡸࡥࡳࡷࡱ࠱ࡩ࡫࡬ࡢࡻࠪঢ়")))
            ]
    def bstack1llll1l11_opy_(self):
        bstack1lll1l11l_opy_ = []
        for spec in self.bstack1lll11ll1_opy_:
            bstack1111llll_opy_ = [spec]
            bstack1111llll_opy_ += self.bstack1lll1l1ll_opy_
            bstack1lll1l11l_opy_.append(bstack1111llll_opy_)
        self.bstack1lll1l11l_opy_ = bstack1lll1l11l_opy_
        return bstack1lll1l11l_opy_
    def bstack1111111l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111l1l11_opy_ = True
            return True
        except Exception as e:
            self.bstack111l1l11_opy_ = False
        return self.bstack111l1l11_opy_
    def bstack11111lll_opy_(self):
        bstack1lllll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡋࡪࡺࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥࡽࡩࡵࡪࡲࡹࡹࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡵࡪࡨࡱࠥࡻࡳࡪࡰࡪࠤࡵࡿࡴࡦࡵࡷࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡭ࡳࡺ࠺ࠡࡖ࡫ࡩࠥࡺ࡯ࡵࡣ࡯ࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࡣࡰ࡮࡯ࡩࡨࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ৞")
        try:
            from browserstack_sdk.bstack11ll1lll_opy_ import bstack11l1llll_opy_
            bstack1lll1l111_opy_ = bstack11l1llll_opy_(bstack11ll11l1_opy_=self.bstack1lll1l1ll_opy_, bstack11l1ll1l_opy_=True)
            if not bstack1lll1l111_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨয়"), False):
                self.logger.error(bstack1lllll1l_opy_ (u"ࠣࡖࡨࡷࡹࠦࡣࡰࡷࡱࡸࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡿࢂࠨৠ").format(bstack1lll1l111_opy_.get(bstack1lllll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨৡ"), bstack1lllll1l_opy_ (u"࡙ࠪࡳࡱ࡮ࡰࡹࡱࠤࡪࡸࡲࡰࡴࠪৢ"))))
                return 0
            count = bstack1lll1l111_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡨࡵࡵ࡯ࡶࠪৣ"), 0)
            test_files = bstack1lll1l111_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴࠩ৤"), [])
            self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡃࡰ࡮࡯ࡩࡨࡺࡥࡥࠢࡾࢁࠥࡺࡥࡴࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠥ࡬ࡩ࡭ࡧࡶࠦ৥").format(count, len(test_files)))
            return count
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥࡲࡹࡳࡺ࠺ࠡࡽࢀࠦ০").format(e))
            return 0
    def bstack1lll1lll1_opy_(self, bstack1llll111l_opy_, bstack11111l1l_opy_):
        bstack11111l1l_opy_[bstack1lllll1l_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨ১")] = self.bstack1lll111l1_opy_
        multiprocessing.set_start_method(bstack1lllll1l_opy_ (u"ࠩࡶࡴࡦࡽ࡮ࠨ২"))
        bstack111l1ll1_opy_ = []
        manager = multiprocessing.Manager()
        bstack1111ll11_opy_ = manager.list()
        if bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৩") in self.bstack1lll111l1_opy_:
            for index, platform in enumerate(self.bstack1lll111l1_opy_[bstack1lllll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ৪")]):
                bstack111l1ll1_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1llll111l_opy_,
                                                            args=(self.bstack1lll1l1ll_opy_, bstack11111l1l_opy_, bstack1111ll11_opy_)))
            bstack111111l1_opy_ = len(self.bstack1lll111l1_opy_[bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৫")])
        else:
            bstack111l1ll1_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1llll111l_opy_,
                                                        args=(self.bstack1lll1l1ll_opy_, bstack11111l1l_opy_, bstack1111ll11_opy_)))
            bstack111111l1_opy_ = 1
        i = 0
        for t in bstack111l1ll1_opy_:
            os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭৬")] = str(i)
            if bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৭") in self.bstack1lll111l1_opy_:
                os.environ[bstack1lllll1l_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩ৮")] = json.dumps(self.bstack1lll111l1_opy_[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৯")][i % bstack111111l1_opy_])
            i += 1
            t.start()
        for t in bstack111l1ll1_opy_:
            t.join()
        return list(bstack1111ll11_opy_)
    @staticmethod
    def bstack111l111l_opy_(driver, bstack1llllll1l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧৰ"), None)
        if item and getattr(item, bstack1lllll1l_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡥࡤࡷࡪ࠭ৱ"), None) and not getattr(item, bstack1lllll1l_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡸࡺ࡯ࡱࡡࡧࡳࡳ࡫ࠧ৲"), False):
            logger.info(
                bstack1lllll1l_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠤࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡸࡲࡩ࡫ࡲࡸࡣࡼ࠲ࠧ৳"))
            bstack1lllllll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1111ll1l_opy_.bstack1lllll11l_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack111l1111_opy_(self):
        bstack1lllll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡺࡨࡦࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡵࡱࠣࡦࡪࠦࡥࡹࡧࡦࡹࡹ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ৴")
        try:
            from browserstack_sdk.bstack11ll1lll_opy_ import bstack11l1llll_opy_
            bstack1lll1llll_opy_ = bstack11l1llll_opy_(bstack11ll11l1_opy_=self.bstack1lll1l1ll_opy_, bstack11l1ll1l_opy_=True)
            if not bstack1lll1llll_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ৵"), False):
                self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡗࡩࡸࡺࠠࡧ࡫࡯ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡿࢂࠨ৶").format(bstack1lll1llll_opy_.get(bstack1lllll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ৷"), bstack1lllll1l_opy_ (u"࡚ࠫࡴ࡫࡯ࡱࡺࡲࠥ࡫ࡲࡳࡱࡵࠫ৸"))))
                return []
            test_files = bstack1lll1llll_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴࠩ৹"), [])
            count = bstack1lll1llll_opy_.get(bstack1lllll1l_opy_ (u"࠭ࡣࡰࡷࡱࡸࠬ৺"), 0)
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡄࡱ࡯ࡰࡪࡩࡴࡦࡦࠣࡿࢂࠦࡴࡦࡵࡷࡷࠥ࡯࡮ࠡࡽࢀࠤ࡫࡯࡬ࡦࡵࠥ৻").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠾ࠥࢁࡽࠣৼ").format(e))
            return []