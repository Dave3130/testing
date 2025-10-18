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
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import (
    bstack1llll1lll11_opy_,
    bstack1llll1ll111_opy_,
    bstack1llllllll1l_opy_,
    bstack1lll1l111l1_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1llll1111ll_opy_, bstack1l1l1lll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_, bstack1lll1llll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1lll1l11ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1111l_opy_ import bstack1llll11111l_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1l111l11ll_opy_ import bstack1l11llll1_opy_, bstack111lll1111_opy_, bstack1111l1ll11_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1l1l11l_opy_(bstack1llll11111l_opy_):
    bstack1lll1ll11l1_opy_ = bstack1l1lll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡴ࡬ࡺࡪࡸࡳࠣჽ")
    bstack1lll1llllll_opy_ = bstack1l1lll1_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤჾ")
    bstack1lll1l1ll11_opy_ = bstack1l1lll1_opy_ (u"ࠦࡳࡵ࡮ࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨჿ")
    bstack1llll11l1l1_opy_ = bstack1l1lll1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᄀ")
    bstack1llll11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡤࡸࡥࡧࡵࠥᄁ")
    bstack1lll11lllll_opy_ = bstack1l1lll1_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡩࡲࡦࡣࡷࡩࡩࠨᄂ")
    bstack1lll1ll1l1l_opy_ = bstack1l1lll1_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᄃ")
    bstack1llll111111_opy_ = bstack1l1lll1_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡴࡶࡤࡸࡺࡹࠢᄄ")
    def __init__(self):
        super().__init__(bstack1llll11l11l_opy_=self.bstack1lll1ll11l1_opy_, frameworks=[bstack1lllll111l1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llllll1111_opy_((bstack1lll1ll11ll_opy_.BEFORE_EACH, bstack1lll1lll11l_opy_.POST), self.bstack1lll1l1l1ll_opy_)
        if bstack1l1l1lll1_opy_():
            TestFramework.bstack1llllll1111_opy_((bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1lll1l111ll_opy_)
        else:
            TestFramework.bstack1llllll1111_opy_((bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1lll1l111ll_opy_)
        TestFramework.bstack1llllll1111_opy_((bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1llll111l1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1lll1ll_opy_ = self.bstack1lll1lllll1_opy_(instance.context)
        if not bstack1lll1lll1ll_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡱࡣࡪࡩ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᄅ") + str(bstack1lllll1llll_opy_) + bstack1l1lll1_opy_ (u"ࠦࠧᄆ"))
            return
        f.bstack1llll1lllll_opy_(instance, bstack1lll1l1l11l_opy_.bstack1lll1llllll_opy_, bstack1lll1lll1ll_opy_)
    def bstack1lll1lllll1_opy_(self, context: bstack1lll1l111l1_opy_, bstack1lll1l1ll1l_opy_= True):
        if bstack1lll1l1ll1l_opy_:
            bstack1lll1lll1ll_opy_ = self.bstack1llll111ll1_opy_(context, reverse=True)
        else:
            bstack1lll1lll1ll_opy_ = self.bstack1llll11ll1l_opy_(context, reverse=True)
        return [f for f in bstack1lll1lll1ll_opy_ if f[1].state != bstack1llll1lll11_opy_.QUIT]
    def bstack1lll1l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1l1ll_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
        if not bstack1llll1111ll_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄇ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠨࠢᄈ"))
            return
        bstack1lll1lll1ll_opy_ = f.get_state(instance, bstack1lll1l1l11l_opy_.bstack1lll1llllll_opy_, [])
        if not bstack1lll1lll1ll_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄉ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠣࠤᄊ"))
            return
        if len(bstack1lll1lll1ll_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡳࡥ࡬࡫࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦᄋ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll1lll_opy_ = bstack1lll1lll1ll_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄌ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠦࠧᄍ"))
            return
        bstack11l1l1l1ll_opy_ = getattr(args[0], bstack1l1lll1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᄎ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l1lll1_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᄏ")).get(bstack1l1lll1_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤᄐ")):
            try:
                page.evaluate(bstack1l1lll1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᄑ"),
                            bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭ᄒ") + json.dumps(
                                bstack11l1l1l1ll_opy_) + bstack1l1lll1_opy_ (u"ࠥࢁࢂࠨᄓ"))
            except Exception as e:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤᄔ"), e)
    def bstack1llll111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1l1ll_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
        if not bstack1llll1111ll_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄕ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠨࠢᄖ"))
            return
        bstack1lll1lll1ll_opy_ = f.get_state(instance, bstack1lll1l1l11l_opy_.bstack1lll1llllll_opy_, [])
        if not bstack1lll1lll1ll_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄗ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠣࠤᄘ"))
            return
        if len(bstack1lll1lll1ll_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡳࡥ࡬࡫࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦᄙ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll1lll_opy_ = bstack1lll1lll1ll_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄚ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠦࠧᄛ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1l11111_opy_, None)
        if not status:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᄜ") + str(bstack1lllll1llll_opy_) + bstack1l1lll1_opy_ (u"ࠨࠢᄝ"))
            return
        bstack1lll1l11l11_opy_ = {bstack1l1lll1_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᄞ"): status.lower()}
        bstack1lll1l1llll_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll111l_opy_, None)
        if status.lower() == bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᄟ") and bstack1lll1l1llll_opy_ is not None:
            bstack1lll1l11l11_opy_[bstack1l1lll1_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᄠ")] = bstack1lll1l1llll_opy_[0][bstack1l1lll1_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᄡ")][0] if isinstance(bstack1lll1l1llll_opy_, list) else str(bstack1lll1l1llll_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l1lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠤᄢ")).get(bstack1l1lll1_opy_ (u"ࠧࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤᄣ")):
            try:
                page.evaluate(
                        bstack1l1lll1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᄤ"),
                        bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࠬᄥ")
                        + json.dumps(bstack1lll1l11l11_opy_)
                        + bstack1l1lll1_opy_ (u"ࠣࡿࠥᄦ")
                    )
            except Exception as e:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡻࡾࠤᄧ"), e)
    def bstack1llll11l1ll_opy_(
        self,
        instance: bstack1lll1llll11_opy_,
        f: TestFramework,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1l1ll_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
        if not bstack1llll1111ll_opy_:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠥࡱࡦࡸ࡫ࡠࡱ࠴࠵ࡾࡥࡳࡺࡰࡦ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦᄨ"))
            return
        bstack1lll1lll1ll_opy_ = f.get_state(instance, bstack1lll1l1l11l_opy_.bstack1lll1llllll_opy_, [])
        if not bstack1lll1lll1ll_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄩ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠧࠨᄪ"))
            return
        if len(bstack1lll1lll1ll_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᄫ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll1lll_opy_ = bstack1lll1lll1ll_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢ࡮ࡣࡵ࡯ࡤࡵ࠱࠲ࡻࡢࡷࡾࡴࡣ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄬ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠣࠤᄭ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1l1lll1_opy_ (u"ࠤࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡕࡼࡲࡨࡀࠢᄮ") + str(timestamp)
        try:
            page.evaluate(
                bstack1l1lll1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᄯ"),
                bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩᄰ").format(
                    json.dumps(
                        {
                            bstack1l1lll1_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᄱ"): bstack1l1lll1_opy_ (u"ࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣᄲ"),
                            bstack1l1lll1_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᄳ"): {
                                bstack1l1lll1_opy_ (u"ࠣࡶࡼࡴࡪࠨᄴ"): bstack1l1lll1_opy_ (u"ࠤࡄࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠨᄵ"),
                                bstack1l1lll1_opy_ (u"ࠥࡨࡦࡺࡡࠣᄶ"): data,
                                bstack1l1lll1_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࠥᄷ"): bstack1l1lll1_opy_ (u"ࠧࡪࡥࡣࡷࡪࠦᄸ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡲ࠵࠶ࡿࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࢁࡽࠣᄹ"), e)
    def bstack1llll1l1111_opy_(
        self,
        instance: bstack1lll1llll11_opy_,
        f: TestFramework,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1l1ll_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1l1l11l_opy_.bstack1lll11lllll_opy_, False):
            return
        self.bstack1llll1llll1_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1l1ll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll1l111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l1l111_opy_)
        req.test_framework_state = bstack1lllll1llll_opy_[0].name
        req.test_hook_state = bstack1lllll1llll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll11lll1_opy_)
        for bstack1lll1lll1l1_opy_ in bstack1lll1l11ll1_opy_.bstack1lll1l1l1l1_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1l1lll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨᄺ")
                if bstack1llll1111ll_opy_
                else bstack1l1lll1_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠢᄻ")
            )
            session.ref = bstack1lll1lll1l1_opy_.ref()
            session.hub_url = bstack1lll1l11ll1_opy_.get_state(bstack1lll1lll1l1_opy_, bstack1lll1l11ll1_opy_.bstack1lll1ll1ll1_opy_, bstack1l1lll1_opy_ (u"ࠤࠥᄼ"))
            session.framework_name = bstack1lll1lll1l1_opy_.framework_name
            session.framework_version = bstack1lll1lll1l1_opy_.framework_version
            session.framework_session_id = bstack1lll1l11ll1_opy_.get_state(bstack1lll1lll1l1_opy_, bstack1lll1l11ll1_opy_.bstack1llll11llll_opy_, bstack1l1lll1_opy_ (u"ࠥࠦᄽ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1lll1ll_opy_ = f.get_state(instance, bstack1lll1l1l11l_opy_.bstack1lll1llllll_opy_, [])
        if not bstack1lll1lll1ll_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄾ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠧࠨᄿ"))
            return
        if len(bstack1lll1lll1ll_opy_) > 1:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅀ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠢࠣᅁ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll1lll_opy_ = bstack1lll1lll1ll_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᅂ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠤࠥᅃ"))
            return
        return page
    def bstack1llll1111l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1lll1l11lll_opy_ = {}
        for bstack1lll1lll1l1_opy_ in bstack1lll1l11ll1_opy_.bstack1lll1l1l1l1_opy_.values():
            caps = bstack1lll1l11ll1_opy_.get_state(bstack1lll1lll1l1_opy_, bstack1lll1l11ll1_opy_.bstack1lll1ll1111_opy_, bstack1l1lll1_opy_ (u"ࠥࠦᅄ"))
        bstack1lll1l11lll_opy_[bstack1l1lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤᅅ")] = caps.get(bstack1l1lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨᅆ"), bstack1l1lll1_opy_ (u"ࠨࠢᅇ"))
        bstack1lll1l11lll_opy_[bstack1l1lll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨᅈ")] = caps.get(bstack1l1lll1_opy_ (u"ࠣࡱࡶࠦᅉ"), bstack1l1lll1_opy_ (u"ࠤࠥᅊ"))
        bstack1lll1l11lll_opy_[bstack1l1lll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧᅋ")] = caps.get(bstack1l1lll1_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣᅌ"), bstack1l1lll1_opy_ (u"ࠧࠨᅍ"))
        bstack1lll1l11lll_opy_[bstack1l1lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢᅎ")] = caps.get(bstack1l1lll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤᅏ"), bstack1l1lll1_opy_ (u"ࠣࠤᅐ"))
        return bstack1lll1l11lll_opy_
    def bstack1lll1l1lll1_opy_(self, page: object, bstack1llll11l111_opy_, args={}):
        try:
            bstack1llll111l11_opy_ = bstack1l1lll1_opy_ (u"ࠤࠥࠦ࠭࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࠩ࠰࠱࠲ࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶ࠭ࠥࢁࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࠣࡲࡪࡽࠠࡑࡴࡲࡱ࡮ࡹࡥࠩࠪࡵࡩࡸࡵ࡬ࡷࡧ࠯ࠤࡷ࡫ࡪࡦࡥࡷ࠭ࠥࡃ࠾ࠡࡽࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵ࠱ࡴࡺࡹࡨࠩࡴࡨࡷࡴࡲࡶࡦࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡿ࡫ࡴ࡟ࡣࡱࡧࡽࢂࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࢀ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࢃࠩࠩࡽࡤࡶ࡬ࡥࡪࡴࡱࡱࢁ࠮ࠨࠢࠣᅑ")
            bstack1llll11l111_opy_ = bstack1llll11l111_opy_.replace(bstack1l1lll1_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨᅒ"), bstack1l1lll1_opy_ (u"ࠦࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶࠦᅓ"))
            script = bstack1llll111l11_opy_.format(fn_body=bstack1llll11l111_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠧࡧ࠱࠲ࡻࡢࡷࡨࡸࡩࡱࡶࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥࡋࡲࡳࡱࡵࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵ࠮ࠣࠦᅔ") + str(e) + bstack1l1lll1_opy_ (u"ࠨࠢᅕ"))