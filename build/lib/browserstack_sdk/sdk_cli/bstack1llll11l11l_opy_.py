# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import (
    bstack1111111l11_opy_,
    bstack1llllll1ll1_opy_,
    bstack111111l111_opy_,
    bstack1llll11l111_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l1llll_opy_, bstack11ll1l1lll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1lllll1ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_, bstack1llll1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll11l1_opy_ import bstack1llll11l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11ll1_opy_ import bstack1lll1ll1111_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack11l11ll11_opy_ import bstack111ll11l11_opy_, bstack11111ll111_opy_, bstack111llll1ll_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1l1lll1_opy_(bstack1lll1ll1111_opy_):
    bstack1lll1lll111_opy_ = bstack1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡴ࡬ࡺࡪࡸࡳࠣᄄ")
    bstack1lll1l11l1l_opy_ = bstack1l_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᄅ")
    bstack1lll1l11lll_opy_ = bstack1l_opy_ (u"ࠦࡳࡵ࡮ࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᄆ")
    bstack1llll11ll1l_opy_ = bstack1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᄇ")
    bstack1lll1ll111l_opy_ = bstack1l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡤࡸࡥࡧࡵࠥᄈ")
    bstack1llll111l1l_opy_ = bstack1l_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡩࡲࡦࡣࡷࡩࡩࠨᄉ")
    bstack1lll1lll11l_opy_ = bstack1l_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᄊ")
    bstack1llll111lll_opy_ = bstack1l_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡴࡶࡤࡸࡺࡹࠢᄋ")
    def __init__(self):
        super().__init__(bstack1lll1l1l11l_opy_=self.bstack1lll1lll111_opy_, frameworks=[bstack1lllll1ll1l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.BEFORE_EACH, bstack1lll1llll1l_opy_.POST), self.bstack1llll1l11ll_opy_)
        if bstack11ll1l1lll_opy_():
            TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.POST), self.bstack1lll1lll1ll_opy_)
        else:
            TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.PRE), self.bstack1lll1lll1ll_opy_)
        TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.POST), self.bstack1lll1l1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1l11ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1ll1l11_opy_ = self.bstack1lll1l111l1_opy_(instance.context)
        if not bstack1lll1ll1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡱࡣࡪࡩ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᄌ") + str(bstack1lllll1ll11_opy_) + bstack1l_opy_ (u"ࠦࠧᄍ"))
            return
        f.bstack1lllll11ll1_opy_(instance, bstack1lll1l1lll1_opy_.bstack1lll1l11l1l_opy_, bstack1lll1ll1l11_opy_)
    def bstack1lll1l111l1_opy_(self, context: bstack1llll11l111_opy_, bstack1llll1l1111_opy_= True):
        if bstack1llll1l1111_opy_:
            bstack1lll1ll1l11_opy_ = self.bstack1llll11llll_opy_(context, reverse=True)
        else:
            bstack1lll1ll1l11_opy_ = self.bstack1lll1ll1ll1_opy_(context, reverse=True)
        return [f for f in bstack1lll1ll1l11_opy_ if f[1].state != bstack1111111l11_opy_.QUIT]
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll1l11ll_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if not bstack1lll1l1llll_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄎ") + str(kwargs) + bstack1l_opy_ (u"ࠨࠢᄏ"))
            return
        bstack1lll1ll1l11_opy_ = f.get_state(instance, bstack1lll1l1lll1_opy_.bstack1lll1l11l1l_opy_, [])
        if not bstack1lll1ll1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄐ") + str(kwargs) + bstack1l_opy_ (u"ࠣࠤᄑ"))
            return
        if len(bstack1lll1ll1l11_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡳࡥ࡬࡫࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦᄒ"))
        bstack1lll1l1l1l1_opy_, bstack1llll1111ll_opy_ = bstack1lll1ll1l11_opy_[0]
        page = bstack1lll1l1l1l1_opy_()
        if not page:
            self.logger.debug(bstack1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄓ") + str(kwargs) + bstack1l_opy_ (u"ࠦࠧᄔ"))
            return
        bstack1l1ll1ll1_opy_ = getattr(args[0], bstack1l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᄕ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᄖ")).get(bstack1l_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤᄗ")):
            try:
                page.evaluate(bstack1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᄘ"),
                            bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭ᄙ") + json.dumps(
                                bstack1l1ll1ll1_opy_) + bstack1l_opy_ (u"ࠥࢁࢂࠨᄚ"))
            except Exception as e:
                self.logger.debug(bstack1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤᄛ"), e)
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll1l11ll_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if not bstack1lll1l1llll_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄜ") + str(kwargs) + bstack1l_opy_ (u"ࠨࠢᄝ"))
            return
        bstack1lll1ll1l11_opy_ = f.get_state(instance, bstack1lll1l1lll1_opy_.bstack1lll1l11l1l_opy_, [])
        if not bstack1lll1ll1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄞ") + str(kwargs) + bstack1l_opy_ (u"ࠣࠤᄟ"))
            return
        if len(bstack1lll1ll1l11_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡳࡥ࡬࡫࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦᄠ"))
        bstack1lll1l1l1l1_opy_, bstack1llll1111ll_opy_ = bstack1lll1ll1l11_opy_[0]
        page = bstack1lll1l1l1l1_opy_()
        if not page:
            self.logger.debug(bstack1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄡ") + str(kwargs) + bstack1l_opy_ (u"ࠦࠧᄢ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1ll1lll_opy_, None)
        if not status:
            self.logger.debug(bstack1l_opy_ (u"ࠧࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᄣ") + str(bstack1lllll1ll11_opy_) + bstack1l_opy_ (u"ࠨࠢᄤ"))
            return
        bstack1lll1l1l111_opy_ = {bstack1l_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᄥ"): status.lower()}
        bstack1lll1lllll1_opy_ = f.get_state(instance, TestFramework.bstack1lll1lll1l1_opy_, None)
        if status.lower() == bstack1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᄦ") and bstack1lll1lllll1_opy_ is not None:
            bstack1lll1l1l111_opy_[bstack1l_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᄧ")] = bstack1lll1lllll1_opy_[0][bstack1l_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᄨ")][0] if isinstance(bstack1lll1lllll1_opy_, list) else str(bstack1lll1lllll1_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᄩ")).get(bstack1l_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᄪ")):
            try:
                page.evaluate(
                        bstack1l_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᄫ"),
                        bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࠬᄬ")
                        + json.dumps(bstack1lll1l1l111_opy_)
                        + bstack1l_opy_ (u"ࠣࡿࠥᄭ")
                    )
            except Exception as e:
                self.logger.debug(bstack1l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡻࡾࠤᄮ"), e)
    def bstack1lll1l1ll11_opy_(
        self,
        instance: bstack1llll1l1l11_opy_,
        f: TestFramework,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll1l11ll_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if not bstack1lll1l1llll_opy_:
            self.logger.debug(
                bstack1lll1ll1l1l_opy_ (u"ࠥࡱࡦࡸ࡫ࡠࡱ࠴࠵ࡾࡥࡳࡺࡰࡦ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦᄯ"))
            return
        bstack1lll1ll1l11_opy_ = f.get_state(instance, bstack1lll1l1lll1_opy_.bstack1lll1l11l1l_opy_, [])
        if not bstack1lll1ll1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄰ") + str(kwargs) + bstack1l_opy_ (u"ࠧࠨᄱ"))
            return
        if len(bstack1lll1ll1l11_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᄲ"))
        bstack1lll1l1l1l1_opy_, bstack1llll1111ll_opy_ = bstack1lll1ll1l11_opy_[0]
        page = bstack1lll1l1l1l1_opy_()
        if not page:
            self.logger.debug(bstack1l_opy_ (u"ࠢ࡮ࡣࡵ࡯ࡤࡵ࠱࠲ࡻࡢࡷࡾࡴࡣ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄳ") + str(kwargs) + bstack1l_opy_ (u"ࠣࠤᄴ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1l_opy_ (u"ࠤࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡕࡼࡲࡨࡀࠢᄵ") + str(timestamp)
        try:
            page.evaluate(
                bstack1l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᄶ"),
                bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩᄷ").format(
                    json.dumps(
                        {
                            bstack1l_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᄸ"): bstack1l_opy_ (u"ࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣᄹ"),
                            bstack1l_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᄺ"): {
                                bstack1l_opy_ (u"ࠣࡶࡼࡴࡪࠨᄻ"): bstack1l_opy_ (u"ࠤࡄࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠨᄼ"),
                                bstack1l_opy_ (u"ࠥࡨࡦࡺࡡࠣᄽ"): data,
                                bstack1l_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࠥᄾ"): bstack1l_opy_ (u"ࠧࡪࡥࡣࡷࡪࠦᄿ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1l_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡲ࠵࠶ࡿࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࢁࡽࠣᅀ"), e)
    def bstack1lll1ll11ll_opy_(
        self,
        instance: bstack1llll1l1l11_opy_,
        f: TestFramework,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1llll1l11ll_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1l1lll1_opy_.bstack1llll111l1l_opy_, False):
            return
        self.bstack1lllll1l111_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1lllll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll11111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        req.test_framework_state = bstack1lllll1ll11_opy_[0].name
        req.test_hook_state = bstack1lllll1ll11_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll11ll11_opy_)
        for bstack1llll1l11l1_opy_ in bstack1llll11l1l1_opy_.bstack1llll11l1ll_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨᅁ")
                if bstack1lll1l1llll_opy_
                else bstack1l_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠢᅂ")
            )
            session.ref = bstack1llll1l11l1_opy_.ref()
            session.hub_url = bstack1llll11l1l1_opy_.get_state(bstack1llll1l11l1_opy_, bstack1llll11l1l1_opy_.bstack1llll111ll1_opy_, bstack1l_opy_ (u"ࠤࠥᅃ"))
            session.framework_name = bstack1llll1l11l1_opy_.framework_name
            session.framework_version = bstack1llll1l11l1_opy_.framework_version
            session.framework_session_id = bstack1llll11l1l1_opy_.get_state(bstack1llll1l11l1_opy_, bstack1llll11l1l1_opy_.bstack1llll11lll1_opy_, bstack1l_opy_ (u"ࠥࠦᅄ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1llll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1ll1l11_opy_ = f.get_state(instance, bstack1lll1l1lll1_opy_.bstack1lll1l11l1l_opy_, [])
        if not bstack1lll1ll1l11_opy_:
            self.logger.debug(bstack1l_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅅ") + str(kwargs) + bstack1l_opy_ (u"ࠧࠨᅆ"))
            return
        if len(bstack1lll1ll1l11_opy_) > 1:
            self.logger.debug(bstack1l_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅇ") + str(kwargs) + bstack1l_opy_ (u"ࠢࠣᅈ"))
        bstack1lll1l1l1l1_opy_, bstack1llll1111ll_opy_ = bstack1lll1ll1l11_opy_[0]
        page = bstack1lll1l1l1l1_opy_()
        if not page:
            self.logger.debug(bstack1l_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᅉ") + str(kwargs) + bstack1l_opy_ (u"ࠤࠥᅊ"))
            return
        return page
    def bstack1lll1l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll111111_opy_ = {}
        for bstack1llll1l11l1_opy_ in bstack1llll11l1l1_opy_.bstack1llll11l1ll_opy_.values():
            caps = bstack1llll11l1l1_opy_.get_state(bstack1llll1l11l1_opy_, bstack1llll11l1l1_opy_.bstack1lll1llllll_opy_, bstack1l_opy_ (u"ࠥࠦᅋ"))
        bstack1llll111111_opy_[bstack1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤᅌ")] = caps.get(bstack1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨᅍ"), bstack1l_opy_ (u"ࠨࠢᅎ"))
        bstack1llll111111_opy_[bstack1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨᅏ")] = caps.get(bstack1l_opy_ (u"ࠣࡱࡶࠦᅐ"), bstack1l_opy_ (u"ࠤࠥᅑ"))
        bstack1llll111111_opy_[bstack1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧᅒ")] = caps.get(bstack1l_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣᅓ"), bstack1l_opy_ (u"ࠧࠨᅔ"))
        bstack1llll111111_opy_[bstack1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢᅕ")] = caps.get(bstack1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤᅖ"), bstack1l_opy_ (u"ࠣࠤᅗ"))
        return bstack1llll111111_opy_
    def bstack1llll111l11_opy_(self, page: object, bstack1lll1l11l11_opy_, args={}):
        try:
            bstack1llll1l111l_opy_ = bstack1l_opy_ (u"ࠤࠥࠦ࠭࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࠩ࠰࠱࠲ࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶ࠭ࠥࢁࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࠣࡲࡪࡽࠠࡑࡴࡲࡱ࡮ࡹࡥࠩࠪࡵࡩࡸࡵ࡬ࡷࡧ࠯ࠤࡷ࡫ࡪࡦࡥࡷ࠭ࠥࡃ࠾ࠡࡽࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵ࠱ࡴࡺࡹࡨࠩࡴࡨࡷࡴࡲࡶࡦࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡿ࡫ࡴ࡟ࡣࡱࡧࡽࢂࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࢀ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࢃࠩࠩࡽࡤࡶ࡬ࡥࡪࡴࡱࡱࢁ࠮ࠨࠢࠣᅘ")
            bstack1lll1l11l11_opy_ = bstack1lll1l11l11_opy_.replace(bstack1l_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᅙ"), bstack1l_opy_ (u"ࠦࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶࠦᅚ"))
            script = bstack1llll1l111l_opy_.format(fn_body=bstack1lll1l11l11_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1l_opy_ (u"ࠧࡧ࠱࠲ࡻࡢࡷࡨࡸࡩࡱࡶࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥࡋࡲࡳࡱࡵࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵ࠮ࠣࠦᅛ") + str(e) + bstack1l_opy_ (u"ࠨࠢᅜ"))