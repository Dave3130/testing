# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1lll111_opy_ import bstack11lll111lll_opy_
from bstack_utils.bstack1111llll_opy_ import bstack11111l1l_opy_
from bstack_utils.helper import bstack1lll1ll111_opy_
import json
class bstack111lll11_opy_:
    _1ll1ll1ll1l_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack1111l11l1l1_opy_ = bstack11lll111lll_opy_(self.config, logger)
        self.bstack1111llll_opy_ = bstack11111l1l_opy_.bstack111l1ll1_opy_(config=self.config)
        self.bstack1111l11l1ll_opy_ = {}
        self.bstack111lllll_opy_ = False
        self.bstack1111l111lll_opy_ = (
            self.__1111l111l1l_opy_()
            and self.bstack1111llll_opy_ is not None
            and self.bstack1111llll_opy_.bstack11111ll1_opy_()
            and config.get(bstack1ll1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫẃ"), None) is not None
            and config.get(bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪẄ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack111l1ll1_opy_(cls, config, logger):
        if cls._1ll1ll1ll1l_opy_ is None and config is not None:
            cls._1ll1ll1ll1l_opy_ = bstack111lll11_opy_(config, logger)
        return cls._1ll1ll1ll1l_opy_
    def bstack11111ll1_opy_(self):
        bstack1ll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡊ࡯ࠡࡰࡲࡸࠥࡧࡰࡱ࡮ࡼࠤࡹ࡫ࡳࡵࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡼ࡮ࡥ࡯࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡑ࠴࠵ࡾࠦࡩࡴࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡕࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡪࡵࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠦࡩࡴࠢࡑࡳࡳ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦẅ")
        return self.bstack1111l111lll_opy_ and self.bstack1111l111l11_opy_()
    def bstack1111l111l11_opy_(self):
        bstack1111l111ll1_opy_ = os.getenv(bstack1ll1l_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪẆ"), self.config.get(bstack1ll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ẇ"), None))
        return bstack1111l111ll1_opy_ in bstack11l11lll11l_opy_
    def __1111l111l1l_opy_(self):
        bstack11ll1l11l11_opy_ = False
        for fw in bstack11l11ll1l11_opy_:
            if fw in self.config.get(bstack1ll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧẈ"), bstack1ll1l_opy_ (u"ࠬ࠭ẉ")):
                bstack11ll1l11l11_opy_ = True
        return bstack1lll1ll111_opy_(self.config.get(bstack1ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪẊ"), bstack11ll1l11l11_opy_))
    def bstack1111l11l111_opy_(self):
        return (not self.bstack11111ll1_opy_() and
                self.bstack1111llll_opy_ is not None and self.bstack1111llll_opy_.bstack11111ll1_opy_())
    def bstack1111l11ll11_opy_(self):
        if not self.bstack1111l11l111_opy_():
            return
        if self.config.get(bstack1ll1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬẋ"), None) is None or self.config.get(bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫẌ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack1ll1l_opy_ (u"ࠤࡗࡩࡸࡺࠠࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡨࡧ࡮ࠨࡶࠣࡻࡴࡸ࡫ࠡࡣࡶࠤࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠠࡰࡴࠣࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠡ࡫ࡶࠤࡳࡻ࡬࡭࠰ࠣࡔࡱ࡫ࡡࡴࡧࠣࡷࡪࡺࠠࡢࠢࡱࡳࡳ࠳࡮ࡶ࡮࡯ࠤࡻࡧ࡬ࡶࡧ࠱ࠦẍ"))
        if not self.__1111l111l1l_opy_():
            self.logger.info(bstack1ll1l_opy_ (u"ࠥࡘࡪࡹࡴࠡࡔࡨࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡩࡡ࡯ࠩࡷࠤࡼࡵࡲ࡬ࠢࡤࡷࠥࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦ࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡪࡴࡡࡣ࡮ࡨࠤ࡮ࡺࠠࡧࡴࡲࡱࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠡࡨ࡬ࡰࡪ࠴ࠢẎ"))
    def bstack1111l11l11l_opy_(self):
        return self.bstack111lllll_opy_
    def bstack111l1lll_opy_(self, bstack1111l1111ll_opy_):
        self.bstack111lllll_opy_ = bstack1111l1111ll_opy_
        self.bstack111ll11l_opy_(bstack1ll1l_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡨࡨࠧẏ"), bstack1111l1111ll_opy_)
    def bstack1llllll1l_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡡࡲࡦࡱࡵࡨࡪࡸ࡟ࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࡡࠥࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡶࡲࡰࡸ࡬ࡨࡪࡪࠠࡧࡱࡵࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬࠴ࠢẐ"))
                return None
            orchestration_strategy = None
            bstack1l1l1111lll_opy_ = self.bstack1111llll_opy_.bstack111llll1l1l_opy_()
            if self.bstack1111llll_opy_ is not None:
                orchestration_strategy = self.bstack1111llll_opy_.bstack1111lll11_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack1ll1l_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡵࡴࡤࡸࡪ࡭ࡹࠡ࡫ࡶࠤࡓࡵ࡮ࡦ࠰ࠣࡇࡦࡴ࡮ࡰࡶࠣࡴࡷࡵࡣࡦࡧࡧࠤࡼ࡯ࡴࡩࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠯ࠤẑ"))
                return None
            self.logger.info(bstack1ll1l_opy_ (u"ࠢࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡹ࡬ࡸ࡭ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡵࡴࡤࡸࡪ࡭ࡹ࠻ࠢࡾࢁࠧẒ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡗࡶ࡭ࡳ࡭ࠠࡄࡎࡌࠤ࡫ࡲ࡯ࡸࠢࡩࡳࡷࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦẓ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(bstack1l1l1111lll_opy_))
            else:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡘࡷ࡮ࡴࡧࠡࡵࡧ࡯ࠥ࡬࡬ࡰࡹࠣࡪࡴࡸࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠲ࠧẔ"))
                self.bstack1111l11l1l1_opy_.bstack11lll1111ll_opy_(test_files, orchestration_strategy, bstack1l1l1111lll_opy_)
                ordered_test_files = self.bstack1111l11l1l1_opy_.bstack11lll111l11_opy_()
            if not ordered_test_files:
                return None
            self.bstack111ll11l_opy_(bstack1ll1l_opy_ (u"ࠥࡹࡵࡲ࡯ࡢࡦࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹࡃࡰࡷࡱࡸࠧẕ"), len(test_files))
            self.bstack111ll11l_opy_(bstack1ll1l_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢẖ"), int(os.environ.get(bstack1ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣẗ")) or bstack1ll1l_opy_ (u"ࠨ࠰ࠣẘ")))
            self.bstack111ll11l_opy_(bstack1ll1l_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦẙ"), int(os.environ.get(bstack1ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦẚ")) or bstack1ll1l_opy_ (u"ࠤ࠴ࠦẛ")))
            self.bstack111ll11l_opy_(bstack1ll1l_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴࡅࡲࡹࡳࡺࠢẜ"), len(ordered_test_files))
            self.bstack111ll11l_opy_(bstack1ll1l_opy_ (u"ࠦࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳࡂࡒࡌࡇࡦࡲ࡬ࡄࡱࡸࡲࡹࠨẝ"), self.bstack1111l11l1l1_opy_.bstack11lll11l1l1_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡡࡲࡦࡱࡵࡨࡪࡸ࡟ࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࡡࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤ࡮ࡤࡷࡸ࡫ࡳ࠻ࠢࡾࢁࠧẞ").format(e))
        return None
    def bstack111ll11l_opy_(self, key, value):
        self.bstack1111l11l1ll_opy_[key] = value
    def bstack11l1l1111_opy_(self):
        return self.bstack1111l11l1ll_opy_