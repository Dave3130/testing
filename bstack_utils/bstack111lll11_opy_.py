# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1lll1ll_opy_ import bstack11ll1ll11l1_opy_
from bstack_utils.bstack1111l1l1_opy_ import bstack1lll1ll11_opy_
from bstack_utils.helper import bstack1llll11lll_opy_
import json
class bstack11111ll1_opy_:
    _1ll1ll1l111_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack1111l111lll_opy_ = bstack11ll1ll11l1_opy_(self.config, logger)
        self.bstack1111l1l1_opy_ = bstack1lll1ll11_opy_.bstack111l111l_opy_(config=self.config)
        self.bstack1111l111l11_opy_ = {}
        self.bstack1111l11l_opy_ = False
        self.bstack1111l1111ll_opy_ = (
            self.__1111l111ll1_opy_()
            and self.bstack1111l1l1_opy_ is not None
            and self.bstack1111l1l1_opy_.bstack1111l111_opy_()
            and config.get(bstack111111l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭Ṿ"), None) is not None
            and config.get(bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬṿ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack111l111l_opy_(cls, config, logger):
        if cls._1ll1ll1l111_opy_ is None and config is not None:
            cls._1ll1ll1l111_opy_ = bstack11111ll1_opy_(config, logger)
        return cls._1ll1ll1l111_opy_
    def bstack1111l111_opy_(self):
        bstack111111l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡅࡱࠣࡲࡴࡺࠠࡢࡲࡳࡰࡾࠦࡴࡦࡵࡷࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡷࡩࡧࡱ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡓ࠶࠷ࡹࠡ࡫ࡶࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡐࡴࡧࡩࡷ࡯࡮ࡨࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠦࡩࡴࠢࡑࡳࡳ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠡ࡫ࡶࠤࡓࡵ࡮ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨẀ")
        return self.bstack1111l1111ll_opy_ and self.bstack1111l111l1l_opy_()
    def bstack1111l111l1l_opy_(self):
        bstack1111l11ll11_opy_ = os.getenv(bstack111111l_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬẁ"), self.config.get(bstack111111l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨẂ"), None))
        return bstack1111l11ll11_opy_ in bstack11l11ll1l1l_opy_
    def __1111l111ll1_opy_(self):
        bstack11ll1l11ll1_opy_ = False
        for fw in bstack11l11lll11l_opy_:
            if fw in self.config.get(bstack111111l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩẃ"), bstack111111l_opy_ (u"ࠧࠨẄ")):
                bstack11ll1l11ll1_opy_ = True
        return bstack1llll11lll_opy_(self.config.get(bstack111111l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬẅ"), bstack11ll1l11ll1_opy_))
    def bstack1111l11l1ll_opy_(self):
        return (not self.bstack1111l111_opy_() and
                self.bstack1111l1l1_opy_ is not None and self.bstack1111l1l1_opy_.bstack1111l111_opy_())
    def bstack1111l11l1l1_opy_(self):
        if not self.bstack1111l11l1ll_opy_():
            return
        if self.config.get(bstack111111l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧẆ"), None) is None or self.config.get(bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ẇ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack111111l_opy_ (u"࡙ࠦ࡫ࡳࡵࠢࡕࡩࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡣࡢࡰࠪࡸࠥࡽ࡯ࡳ࡭ࠣࡥࡸࠦࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠢࡲࡶࠥࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠣ࡭ࡸࠦ࡮ࡶ࡮࡯࠲ࠥࡖ࡬ࡦࡣࡶࡩࠥࡹࡥࡵࠢࡤࠤࡳࡵ࡮࠮ࡰࡸࡰࡱࠦࡶࡢ࡮ࡸࡩ࠳ࠨẈ"))
        if not self.__1111l111ll1_opy_():
            self.logger.info(bstack111111l_opy_ (u"࡚ࠧࡥࡴࡶࠣࡖࡪࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡤࡣࡱࠫࡹࠦࡷࡰࡴ࡮ࠤࡦࡹࠠࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨ࠳ࠦࡐ࡭ࡧࡤࡷࡪࠦࡥ࡯ࡣࡥࡰࡪࠦࡩࡵࠢࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠣࡪ࡮ࡲࡥ࠯ࠤẉ"))
    def bstack1111l11l11l_opy_(self):
        return self.bstack1111l11l_opy_
    def bstack1lll1llll_opy_(self, bstack1111l11l111_opy_):
        self.bstack1111l11l_opy_ = bstack1111l11l111_opy_
        self.bstack111111ll_opy_(bstack111111l_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡪࡪࠢẊ"), bstack1111l11l111_opy_)
    def bstack11l11l1l_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack111111l_opy_ (u"ࠢ࡜ࡴࡨࡳࡷࡪࡥࡳࡡࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࡣࠠࡏࡱࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡱࡴࡲࡺ࡮ࡪࡥࡥࠢࡩࡳࡷࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧ࠯ࠤẋ"))
                return None
            orchestration_strategy = None
            bstack1l11lllll1l_opy_ = self.bstack1111l1l1_opy_.bstack11l111l1111_opy_()
            if self.bstack1111l1l1_opy_ is not None:
                orchestration_strategy = self.bstack1111l1l1_opy_.bstack111l111ll_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack111111l_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡷࡶࡦࡺࡥࡨࡻࠣ࡭ࡸࠦࡎࡰࡰࡨ࠲ࠥࡉࡡ࡯ࡰࡲࡸࠥࡶࡲࡰࡥࡨࡩࡩࠦࡷࡪࡶ࡫ࠤࡹ࡫ࡳࡵࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠱ࠦẌ"))
                return None
            self.logger.info(bstack111111l_opy_ (u"ࠤࡕࡩࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡻ࡮ࡺࡨࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡷࡶࡦࡺࡥࡨࡻ࠽ࠤࢀࢃࠢẍ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack111111l_opy_ (u"࡙ࠥࡸ࡯࡮ࡨࠢࡆࡐࡎࠦࡦ࡭ࡱࡺࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨẎ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(bstack1l11lllll1l_opy_))
            else:
                self.logger.debug(bstack111111l_opy_ (u"࡚ࠦࡹࡩ࡯ࡩࠣࡷࡩࡱࠠࡧ࡮ࡲࡻࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠴ࠢẏ"))
                self.bstack1111l111lll_opy_.bstack11lll11l111_opy_(test_files, orchestration_strategy, bstack1l11lllll1l_opy_)
                ordered_test_files = self.bstack1111l111lll_opy_.bstack11lll111l1l_opy_()
            if not ordered_test_files:
                return None
            self.bstack111111ll_opy_(bstack111111l_opy_ (u"ࠧࡻࡰ࡭ࡱࡤࡨࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴࡅࡲࡹࡳࡺࠢẐ"), len(test_files))
            self.bstack111111ll_opy_(bstack111111l_opy_ (u"ࠨ࡮ࡰࡦࡨࡍࡳࡪࡥࡹࠤẑ"), int(os.environ.get(bstack111111l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥẒ")) or bstack111111l_opy_ (u"ࠣ࠲ࠥẓ")))
            self.bstack111111ll_opy_(bstack111111l_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࡏࡱࡧࡩࡸࠨẔ"), int(os.environ.get(bstack111111l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡄࡑࡘࡒ࡙ࠨẕ")) or bstack111111l_opy_ (u"ࠦ࠶ࠨẖ")))
            self.bstack111111ll_opy_(bstack111111l_opy_ (u"ࠧࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡇࡴࡻ࡮ࡵࠤẗ"), len(ordered_test_files))
            self.bstack111111ll_opy_(bstack111111l_opy_ (u"ࠨࡳࡱ࡮࡬ࡸ࡙࡫ࡳࡵࡵࡄࡔࡎࡉࡡ࡭࡮ࡆࡳࡺࡴࡴࠣẘ"), self.bstack1111l111lll_opy_.bstack11ll1llll1l_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack111111l_opy_ (u"ࠢ࡜ࡴࡨࡳࡷࡪࡥࡳࡡࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡸࡣࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡦࡰࡦࡹࡳࡦࡵ࠽ࠤࢀࢃࠢẙ").format(e))
        return None
    def bstack111111ll_opy_(self, key, value):
        self.bstack1111l111l11_opy_[key] = value
    def bstack111ll11ll_opy_(self):
        return self.bstack1111l111l11_opy_